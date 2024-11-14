from ninja import NinjaAPI
from .models import GarbageSensor
from .schemas import GarbageSensorRequestSchema, UpdateStatusSchema
from django.shortcuts import get_object_or_404
from twilio.rest import Client
import os
from typing import List
from .schemas import GarbageSensorDataSchema

garbage = NinjaAPI(urls_namespace="garbage")

# Initialize Twilio client
client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

# Endpoint for garbage overflow alert
@garbage.post("/sensor_alert", response={200: str})
def garbage_sensor_alert(request, payload: GarbageSensorRequestSchema):
    """Receive garbage alert and send SMS to authorities."""
    sensor = get_object_or_404(GarbageSensor, sensor_id=payload.sensor_id)

    # Update status to 'Overflowed'
    sensor.status = 'Overflowed'
    sensor.save()

    # Send SMS notification
    message_body = f"Garbage Overflow Alert! Location: {sensor.location} (Sensor ID: {sensor.sensor_id})"
    
    client.messages.create(
        body=message_body,
        from_=os.getenv('TWILIO_PHONE_NUMBER'),
        to=os.getenv('AUTHORITY_PHONE_NUMBER')
    )

    return "Overflow alert sent to authorities."

# Endpoint to reset garbage status to 'Normal'
@garbage.post("/reset_status", response={200: str})
def reset_garbage_status(request, payload: UpdateStatusSchema):
    """Reset the garbage status to 'Normal'."""
    sensor = get_object_or_404(GarbageSensor, sensor_id=payload.sensor_id)
    sensor.status = payload.status
    sensor.save()

    return f"Status for Sensor {sensor.sensor_id} updated to {sensor.status}."

@garbage.get("/all_sensors", response=List[GarbageSensorDataSchema])
def get_all_garbage_sensors(request):
    """Retrieve all garbage sensor data."""
    sensors = GarbageSensor.objects.all()
    return sensors

