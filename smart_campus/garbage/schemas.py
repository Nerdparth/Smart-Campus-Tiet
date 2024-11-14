from ninja import Schema

class GarbageSensorRequestSchema(Schema):
    sensor_id: int  # Only the sensor ID will be sent

class UpdateStatusSchema(Schema):
    sensor_id: int
    status: str  # "Normal" or "Overflowed"

class GarbageSensorDataSchema(Schema):
    sensor_id: int
    location: str
    status: str