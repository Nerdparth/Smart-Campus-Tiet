# parking_report/api.py
from ninja import NinjaAPI
from .models import ParkingData
from .schemas import ParkingDataSchema, CreateParkingDataSchema
from typing import List
from django.shortcuts import get_object_or_404

app2 = NinjaAPI(urls_namespace="parking_management")


@app2.post("/add", response=ParkingDataSchema)
def add_parking_data(request, payload: CreateParkingDataSchema):
    """Add a new parking data entry."""
    parking_data = ParkingData.objects.create(**payload.dict())
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
