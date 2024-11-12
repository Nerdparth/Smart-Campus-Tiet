# weather_report/api.py
from ninja import Router
from .models import SensorData
from .schemas import SensorDataSchema, CreateSensorDataSchema
from django.shortcuts import get_object_or_404

router = Router()

# POST route to add new sensor data
@router.post("/add", response={201: SensorDataSchema})
def add_sensor_data(request, payload: CreateSensorDataSchema):
    sensor_data = SensorData.objects.create(**payload.dict())
    return sensor_data

# GET route to fetch all sensor data
@router.get("/data", response=list[SensorDataSchema])
def get_all_sensor_data(request):
    return SensorData.objects.all()

# GET route to fetch data by ID
@router.get("/data/{id}", response=SensorDataSchema)
def get_sensor_data(request, id: int):
    sensor_data = get_object_or_404(SensorData, id=id)
    return sensor_data
