from django.shortcuts import render
from meetings.models import Meeting
from django.http import HttpResponse


# Create your views here.
def meeting_details(request, id):
    try:
        meeting = Meeting.objects.get(pk=id)
        return render(request, "meetings/meeting_details.html", 
                      {"meeting": meeting})
    except Meeting.DoesNotExist:
        return HttpResponse("404: not found :(")
    