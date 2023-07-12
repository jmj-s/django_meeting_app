from django.shortcuts import render, redirect
from meetings.models import Meeting
from django.http import HttpResponse
from django.forms import modelform_factory


# Create your views here.
def meeting_details(request, id):
    try:
        meeting = Meeting.objects.get(pk=id)
        return render(request, "meetings/meeting_details.html", 
                      {"meeting": meeting})
    except Meeting.DoesNotExist:
        return HttpResponse("404: not found :(")

def new_meeting(request):
        #creates a class using the modelform_factory function. Passes in Meeting model and chooses to excludeno fields.
        MeetingForm = modelform_factory(Meeting, exclude=[])

        if request.method == "POST":
            form = MeetingForm(request.POST)
            if form.is_valid():
                    form.save()
                    return redirect("welcome")
        else:
            form = MeetingForm()

        return render(request, 'meetings/new.html', {"form": form}) 