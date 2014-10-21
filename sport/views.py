from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from django.views.decorators.csrf import csrf_exempt
import json

from sport.models import Sport

from django.shortcuts import render
from django import forms

# GET requests

# will delete this later--just a sanity check
def index(request):
    return HttpResponse("Hello, world. You're at the Sport index.")
"""

@csrf_exempt      
def showCalendar(request, sportname=""):
	sportInfo = Sport.objects.get(id=sportname)
	return render(request, 'calendar.html', {'sportInfo': sportInfo})


Figure out how this is gonna work
@csrf_exempt      
def viewAllSports(request):
	return render(request, 'calendar.html', {'sportInfo': sportInfo})


# POST requests
@csrf_exempt
def addGame(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(Sport.addGame(data)), content_type="application/json")


Will be implemented in future iteration:
@csrf_exempt
def addSport(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(Game.addSport(data)), content_type="application/json")
"""