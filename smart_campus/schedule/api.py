from ninja import NinjaAPI
from .models import Schedule
from .schemas import ScheduleEntrySchema, ScheduleListSchema
from django.shortcuts import get_object_or_404
from typing import List

schedule = NinjaAPI(urls_namespace="schedule_api")


@schedule.post("/set_schedule", response={200: str})
def set_schedule(request, payload: ScheduleEntrySchema):
    """Add or update a schedule entry."""
    entry, created = Schedule.objects.update_or_create(
        day=payload.day,
        time=payload.time,
        defaults={"subject": payload.subject},
    )

    if created:
        return "Schedule entry created successfully."
    else:
        return "Schedule entry updated successfully."


@schedule.get("/get_schedule", response=List[ScheduleListSchema])
def get_schedule(request):
    """Retrieve all schedule entries."""
    return Schedule.objects.all()
