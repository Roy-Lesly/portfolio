from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.WelcomeView, name='resumeWelcome'),

    ]