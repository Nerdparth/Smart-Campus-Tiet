from ninja import NinjaAPI
from .models import Meeting
from .schemas import MeetingURLSchema

meeting = NinjaAPI(urls_namespace="meeting_api")


@meeting.post("/set_url", response={200: str})
def set_meeting_url(request, payload: MeetingURLSchema):
    """Store or update the meeting URL."""
    meeting_instance, created = Meeting.objects.update_or_create(
        id=1,  # Ensure only one record exists
        defaults={"url": payload.url},
    )
    
    if created:
        return "Meeting URL saved successfully."
    else:
        return "Meeting URL updated successfully."
