"""
URL configuration for smart_campus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library_management.api import app  # Assume this is another NinjaAPI
from ninja import NinjaAPI
from weather_report.api import router as weather_router

# Set unique urls_namespace for each API instance
app.urls_namespace = "library_api"  # Ensure unique namespace for library_management
api = NinjaAPI(urls_namespace="weather_api")  # Unique namespace for weather_report
api.add_router("/weather", weather_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", app.urls),  # Separate namespace for library API
    path("api/", api.urls),  # Separate namespace for weather API
]
