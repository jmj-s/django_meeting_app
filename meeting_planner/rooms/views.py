from django.shortcuts import render
from meetings.models import Meeting
from rooms.models import Room
from django.http import HttpResponse


# Create your views here.
def room_list(request):
    try:
        rooms = Room.objects.all()
        return render(request, "rooms/all_rooms.html", 
                      {"rooms": rooms})
    except Meeting.DoesNotExist:
        return HttpResponse("404: not found :(")
    