from django.contrib import admin
from django.urls import path, include
import resume.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("resume.urls")),
]
