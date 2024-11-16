from ninja import Schema

class ScheduleEntrySchema(Schema):
    day: str  # Day of the week
    time: str  # Time slot
    subject: str  # Selected subject

class ScheduleListSchema(Schema):
    day: str
    time: str
    subject: str
