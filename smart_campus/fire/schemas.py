from ninja import Schema

class FireSensorDataSchema(Schema):
    sensor_id: int
    fire_hazard_level: int  # 1: low, 2: medium, 3: high
    smoke_level: float      # Smoke level, above 400 indicates fire risk
    temp_level: float       # Temperature level, above 1850 indicates high heat

class ManualFireReportSchema(Schema):
    location: str  # Location provided by user through frontend form
