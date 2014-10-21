from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from django.views.decorators.csrf import csrf_exempt
import json

from game.models import Game

from django.shortcuts import render
from django import forms

# GET requests

# will delete this later--just a sanity check
def index(request):
    return HttpResponse("Hello, world. You're at the Game index.")
"""
    
@csrf_exempt      
def getGamePage(request, gameName=''):
	gameInfo = Game.objects.get(id=gameName)
	return render(request, 'game.html', {'gameinfo': gameInfo})


# POST requests
@csrf_exempt      
def create(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(Game.create(data)), content_type="application/json")


@csrf_exempt	
def addPlayer(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(Game.addPlayer(data)), content_type="application/json")

@csrf_exempt	
def removePlayer(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(Game.removePlayer(data)), content_type="application/json")

@csrf_exempt      
def invite(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(Game.invite(data)), content_type="application/json")


@csrf_exempt	
def timeChange(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(Game.timeChange(data)), content_type="application/json")

@csrf_exempt      
def locationChange(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(Game.locationChange(data)), content_type="application/json")
"""