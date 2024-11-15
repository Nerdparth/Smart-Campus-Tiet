# parking_report/api.py
from ninja import NinjaAPI
from .models import ParkingData
from .schemas import ParkingDataSchema, CreateParkingDataSchema
from typing import List
from django.shortcuts import get_object_or_404

app2 = NinjaAPI(urls_namespace="parking_management")

@app2.post("/add_or_update", response=ParkingDataSchema)
def add_or_update_parking_data(request, payload: CreateParkingDataSchema):
    """Add or update parking data entry based on sensor_id."""

    # Get all records for the given sensor_id, ordered by timestamp, skipping the latest one
    old_records = ParkingData.objects.filter(sensor_id=payload.sensor_id).order_by('-timestamp')[1:]
    
    # Delete old records by their IDs
    old_record_ids = old_records.values_list('id', flat=True)
    ParkingData.objects.filter(id__in=old_record_ids).delete()

    # Update or create the latest record
    parking_data, created = ParkingData.objects.update_or_create(
        sensor_id=payload.sensor_id,
        defaults={
            "sensor_location": payload.sensor_location,
            "parking_status": payload.parking_status,
        }
    )
    print(f"status of {payload.sensor_id} changed to {payload.parking_status} at {payload.sensor_location}")
    return parking_data


@app2.get("/list", response=List[ParkingDataSchema])
def list_parking_data(request):
    """Retrieve a list of all parking data entries."""
    return ParkingData.objects.all()


@app2.get("/get/{sensor_id}", response=ParkingDataSchema)
def get_parking_data(request, sensor_id: int):
    """Retrieve the latest parking data for a specific sensor."""
    parking_data = (
        ParkingData.objects.filter(sensor_id=sensor_id).order_by("-timestamp").first()
    )
    if not parking_data:
        return {"detail": "Data not found"}, 404
    return parking_data
