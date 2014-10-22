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

@csrf_exempt      
def create(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		name = data["name of game"]
		host = data["creator of game"]
		sport = data["sport"]
		time = data["location"]
		location = data["time"]

		rval = Game.createGame(name, host, sport, time, location)

		resdata = { "status code" : rval}

		return HttpResponse(json.dumps(resdata), content_type="application/json")


@csrf_exempt	
def addPlayer(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		game = data["game"]
		newPlayer = data["newPlayer"]

		rval = Game.addPlayer(game, newPlayer)

		resdata = { "status code" : rval}

		return HttpResponse(json.dumps(resdata), content_type="application/json")

@csrf_exempt	
def removePlayer(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		game = data["game"]
		player = data["player"]

		rval = Game.removePlayer(game, player)

		resdata = { "status code" : rval}

		return HttpResponse(json.dumps(resdata), content_type="application/json")

@csrf_exempt      
def invite(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		game = data["game"]
		inviter = data["inviter"]
		invitee = data["invitee"]

		rval = Game.invitePlayer(game, inviter, invitee)

		resdata = { "status code" : rval}

		return HttpResponse(json.dumps(resdata), content_type="application/json")


@csrf_exempt	
def timeChange(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		game = data["game"]
		newTime = data["newTime"]

		rval = Game.gameTimeChange(game, newTime)

		resdata = { "status code" : rval}

		return HttpResponse(json.dumps(resdata), content_type="application/json")

@csrf_exempt      
def locationChange(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		game = data["game"]
		newLocation = data["newLocation"]

		rval = Game.gameLocationChange(game, newLocation)

		resdata = { "status code" : rval}

		return HttpResponse(json.dumps(resdata), content_type="application/json")
