from ninja import ModelSchema, Schema
from .models import Events, Attendees


class AddEventSchema(ModelSchema):
    class Meta:
        model = Events
        fields = "__all__"


class DeleteEventSchema(Schema):
    event_name: str


class RegisterEventSchema(Schema):
    event_name: str
    name: str
    email: str
    semester: str

class EventsCountSchema(Schema):
    events_count : int
    upcoming_events_count : int
