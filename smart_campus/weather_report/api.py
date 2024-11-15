from ninja import NinjaAPI
from .models import SensorData
from .schemas import SensorDataSchema, CreateSensorDataSchema
from django.shortcuts import get_object_or_404

router = NinjaAPI(urls_namespace="weather_api")


# POST route to update sensor data
@router.post("/update", response={201: SensorDataSchema})
def update_sensor_data(request, payload: CreateSensorDataSchema):
    """Update the latest sensor data entry or create it if none exists."""
    sensor_data, created = SensorData.objects.update_or_create(
        id=1,  # Ensures there's only one record to update
        defaults={
            "air_quality": payload.air_quality,
            "air_humidity": payload.air_humidity,
            "temperature": payload.temperature,
        }
    )
    print(f"response recieved {payload.air_quality},{payload.air_humidity},{payload.temperature}")
    return sensor_data


# GET route to fetch the latest sensor data
@router.get("/data", response=SensorDataSchema)
def get_latest_sensor_data(request):
    """Retrieve the latest sensor data entry."""
    sensor_data = get_object_or_404(SensorData, id=1)
    return sensor_data
