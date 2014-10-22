from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from django.views.decorators.csrf import csrf_exempt
import json

from users.models import User

from django.shortcuts import render
from django import forms


# will delete this later--just a sanity check
def index(request):
    return HttpResponse("Hello, world. You're at the User index.")

# GET requests
def home(request):
    return render(request, 'login.html')
   
def viewAllPlayers(request):
	players = User.objects.all()
	return render(request, 'users/players.html', {'players': players})

def viewMyNotifications(request):
	notifications = {} # fill this in
	return render(request, '???.html', {'notifications': notifications})

def viewNewsfeed(request):
	events = {} # fill this in
	return render(request, '???.html', {'events': events})

def viewMyFriends(request):
	players = User.objects.all() #change this to get user's friends
	return render(request, '???.html', {'friends': friends})

def getUserPage(request, username=""):
	# will want to make it so if username=cookie.username it redirects to user/myprofile
	#userInfo = User.objects.get(id=username)
	#return render(request, 'userprofile.html', {'userInfo': userInfo})
	url = "http://addyosmani.com/blog/wp-content/uploads/2013/04/unicorn.jpg"
	name = "Lizzie"
	lname = "Prader"
	uname = "lprader"
	return render(request, 'users/userprofile.html', {"username": uname, "firstName":name, "lastName": lname, "userIcon": url})
    
def getSelfProfile(request):
	userInfo = User.objects.get(id=username) #fix this up
	return render(request, 'myprofile.html', {'userInfo': userInfo})

def getSelfGames(request, username=""):
	# will want to make it so if username=cookie.username it redirects to user/myprofile
	user = User.objects.get(id=username)
	userGames = user.games
	return render(request, 'mygames.html', {'gameList': userGames})
    
"""
# POST requests
@csrf_exempt      
def register(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.register(data)), content_type="application/json")


@csrf_exempt	
def login(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.login(data)), content_type="application/json")

@csrf_exempt	
def requestFriend(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.requestFriend(data)), content_type="application/json")

@csrf_exempt      
def confirmFriendRequest(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.confirmFriendRequest(data)), content_type="application/json")


@csrf_exempt	
def rejectFriendRequest(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.rejectFriendRequest(data)), content_type="application/json")

@csrf_exempt      
def removeFriend(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.removeFriend(data)), content_type="application/json")

@csrf_exempt	
def joinGame(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.joinGame(data)), content_type="application/json")

@csrf_exempt      
def unjoinGame(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.unjoinGame(data)), content_type="application/json")

@csrf_exempt	
def changeIcon(request):
	if request.method == 'POST':
		data = json.loads(request.body.encode(encoding='UTF-8'))
		return HttpResponse(json.dumps(User.changeIcon(data)), content_type="application/json")

"""
