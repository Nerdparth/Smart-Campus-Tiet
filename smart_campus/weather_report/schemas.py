# weather_report/schemas.py
from ninja import Schema
from datetime import datetime


class SensorDataSchema(Schema):
    air_quality: int
    air_humidity: float
    temperature: float
    timestamp: datetime


class CreateSensorDataSchema(Schema):
    air_quality: int
    air_humidity: float
    temperature: float
