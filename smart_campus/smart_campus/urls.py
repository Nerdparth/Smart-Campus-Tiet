from django.contrib import admin
from django.urls import path
from library_management.api import app  # Assume this is another NinjaAPI
from weather_report.api import router
from parking_management.api import app2
from landing_page.views import landing
from event_management.api import app3
from fire.api import fire

# Set unique urls_namespace for each API instance
# app.urls_namespace = "library_api"  # Ensure unique namespace for library_management
# api = NinjaAPI(urls_namespace="weather_api")  # Unique namespace for weather_report
# api.add_router("/weather", )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", app.urls),  # Separate namespace for library API
    # path("api/", api.urls),  # Separate namespace for weather API
    path("weather-api/", router.urls),
    path("parking-management/", app2.urls),
    path("events-api/", app3.urls),
    path("", landing, name="index"),
    path("fire-api/",fire.urls)
]
