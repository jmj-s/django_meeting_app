from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting
from rooms.models import Room

# Create your views here.

def welcome(request):
    return render(request,"website/home.html", 
                  {"num_meetings": Meeting.objects.count(),
                   "num_rooms": Room.objects.count(),
                   "meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("The current date and time is: " +  str(datetime.now()))

def about(request):
    return HttpResponse("<p>Greetings! My name is Stuart.</p>")