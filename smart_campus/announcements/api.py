from ninja import NinjaAPI
from .models import Announcement
from .schemas import AnnouncementSchema
from django.shortcuts import get_object_or_404

announcements = NinjaAPI(urls_namespace="announcements_api")


@announcements.post("/set_announcement", response={200: str})
def set_announcement(request, payload: AnnouncementSchema):
    """Store or update the announcement."""
    announcement, created = Announcement.objects.update_or_create(
        id=1,  # Ensure only one record exists
        defaults={"content": payload.content},
    )
    
    if created:
        return "Announcement created successfully."
    else:
        return "Announcement updated successfully."


@announcements.get("/get_announcement", response=AnnouncementSchema)
def get_announcement(request):
    """Retrieve the current announcement."""
    announcement = get_object_or_404(Announcement, id=1)
    return {"content": announcement.content}
