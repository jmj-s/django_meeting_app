from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

def date(request):
    return HttpResponse("The current date and time is: " +  str(datetime.now()))

def about(request):
    return HttpResponse("<p>Greetings! My name is Stuart.</p>")