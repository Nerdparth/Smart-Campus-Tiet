from ninja import NinjaAPI
from .schemas import AddEventSchema, DeleteEventSchema, RegisterEventSchema, EventsCountSchema
from .models import Events, Attendees
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404


app3 = NinjaAPI(urls_namespace="event_management")


@app3.post("/add-event", response=AddEventSchema)
def add_event(request, details: AddEventSchema):
    event_name = details.event_name
    description = details.description
    hosted_by = details.hosted_by
    datetime = details.datetime
    if Events.objects.filter(event_name=event_name).exists():
        return JsonResponse(
            {"error": "event name already exists, choose a different event name"}
        )
    else:
        event = Events.objects.create(
            event_name=event_name,
            description=description,
            hosted_by=hosted_by,
            datetime=datetime,
        )
    return JsonResponse({"message": "event created successfully"})


@app3.get("/get-all-events")
def get_all_events(request):
    data = []
    events = Events.objects.all()
    for event in events:
        data.append(
            {
                "event_name": event.event_name,
                "description": event.description,
                "hosted_by": event.hosted_by,
                "datetime": event.datetime,
            }
        )
    return data


@app3.get("/get-upcoming-events")
def upcoming_events(request):
    data = []
    upcoming_events = Events.objects.filter(datetime__gt=timezone.now())
    for events in upcoming_events:
        data.append(
            {
                "event_name": events.event_name,
                "description": events.description,
                "hosted_by": events.hosted_by,
                "datetime": events.datetime,
            }
        )

    return data


@app3.get("/get-event/{event_name}")
def get_event(request, event_name: str):
    if not Events.objects.filter(event_name=event_name).exists():
        return JsonResponse({"error": "no such event exists in our db"})
    event_data_getter = Events.objects.get(event_name=event_name)
    event_data = {
        "event_name": event_data_getter.event_name,
        "description": event_data_getter.description,
        "hosted_by": event_data_getter.hosted_by,
        "datetime": event_data_getter.datetime,
    }
    return event_data


@app3.post("/delete-event", response=DeleteEventSchema)
def delete_event(request, details: DeleteEventSchema):
    event_name = details.event_name
    event = Events.objects.filter(event_name=event_name).delete()
    return JsonResponse({"message": "Event deleted from our db"})


@app3.post("/register-for-event", response=RegisterEventSchema)
def register_for_event(request, details: RegisterEventSchema):

    event = get_object_or_404(
        Events, event_name=details.event_name, datetime__gt=timezone.now()
    )

    if Attendees.objects.filter(event_name=event, email=details.email).exists():
        return JsonResponse(
            {"error": "You are already registered for this event"}, status=400
        )

    attendee = Attendees.objects.create(
        event_name=event,
        name=details.name,
        email=details.email,
        semester=details.semester,
    )

    return JsonResponse({"message": "Registered for the event successfully"})


@app3.get("/get-all-attendees/{event_name}")
def get_all_attendees(request, event_name: str):
    event_instance = get_object_or_404(Events, event_name=event_name)
    attendees = Attendees.objects.filter(event_name=event_instance)
    data = []
    for attendee in attendees:
        data.append(
            {
                "name": attendee.name,
                "email": attendee.email,
                "semester": attendee.semester,
            }
        )
    return data

@app3.get("/events-count", response= EventsCountSchema)
def get_events_count(request):
    total_events = Events.objects.all().count()
    upcoming_events = Events.objects.filter(datetime__gt=timezone.now()).count()
    return JsonResponse({"event_count" : total_events, "upcoming_events_count" : upcoming_events})
