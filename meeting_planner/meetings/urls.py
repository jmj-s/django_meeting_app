from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.meeting_details, name="meeting_details"),
    path('new', views.new_meeting, name="new_meeting")
]