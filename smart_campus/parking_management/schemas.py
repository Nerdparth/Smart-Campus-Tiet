from ninja import Schema
from datetime import datetime


# Output Schema
class ParkingDataSchema(Schema):
    id: int
    sensor_id: int
    sensor_location: str
    parking_status: bool
    timestamp: datetime


# Input Schema
class CreateParkingDataSchema(Schema):
    sensor_id: int
    sensor_location: str
    parking_status: bool
