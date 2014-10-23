from django import forms
from django.db import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, UserManager

class UserProfile(User):
	SUCCESS = 1
	USER_EXISTS = -1
	INVALID_USERNAME = -2
	INVALID_PASSWORD = -3
	INVALID_EMAIL = -4
	INVALID_FRIEND_USERNAME = -5
	REQUEST_DNE = -6 
	USER_WAS_NOT_FRIEND = -7
	GAME_DNE = -8
	INVALID_CREDENTIALS = -9
	REQUEST_EXISTS = -10
	ALREADY_FRIENDS = -11
	MAX_USERNAME_LENGTH = 128
	MAX_PASSWORD_LENGTH = 128

	#username, password, email, first_name, last_name are default fields of User class.

	#icon = models.ImageField(blank=True, null=True)
	friends = models.ManyToManyField('self', blank=True, default=None)

	objects = UserManager() #UserProfile.objects.create(...)
	
	def __unicode__(self):
		return self.username


	def registerUser(self, username, password, email, fName, lName):
		check = self.validate_user(username, password, email)
		if (check == UserProfile.SUCCESS):
			user = UserProfile.objects.create_user(username=username, password=password, 
				email=email, first_name=fName, last_name=lName)
			user.save()
		return check #check is the errCode

	def checkTest(self, username, password):
		temp = None
		try:
			temp = UserProfile.objects.get(username=username)
		except Exception as e:
			print(e)
		print(temp)
		user = authenticate(username=username, password=password)
		if user is not None:
			print("yay")
		else:
			print("Wtf")

	def loginUser(self, request, user):
		login(request, user)

	def logoutUser(self, request):
		logout(request)


	def add_friend(self, friend):
		self.friends.add(friend)

	def remove_friend(self, friend):
		self.friends.remove(friend)

	def auth(self, username, password):
		user = authenticate(username=username, password=password)
		return user

	def TESTAPI_reset(self):
		UserProfile.objects.all().delete()
		FriendRequest.objects.all().delete()
		return UserProfile.SUCCESS

	def validate_user(self, username, password, email):
		if username is None:
			return UserProfile.INVALID_USERNAME
		elif email is None:
			return UserProfile.INVALID_EMAIL
	
		if len(username) == 0 or len(username) > UserProfile.MAX_USERNAME_LENGTH:
			return UserProfile.INVALID_USERNAME
		elif len(password) > UserProfile.MAX_PASSWORD_LENGTH:
			return UserProfile.INVALID_PASSWORD
		
		user_exists = UserProfile.checkUser(username)
		if user_exists is not None:
			return UserProfile.USER_EXISTS
		
		f = forms.EmailField()
		try:
			email = f.clean(email)
		except forms.ValidationError as e:
			return UserProfile.INVALID_EMAIL
		return UserProfile.SUCCESS

	@classmethod
	def checkUser(self, username):
		try:
			user = UserProfile.objects.get(username=username)
		except UserProfile.DoesNotExist as e:
			user = None
		return user


class FriendRequest(models.Model):
		
	user = models.CharField(max_length=UserProfile.MAX_USERNAME_LENGTH)
	friend = models.CharField(max_length=UserProfile.MAX_USERNAME_LENGTH)
	objects = models.Manager()

	@classmethod
	def verify(self, username, friend):
		user = UserProfile.checkUser(username)
		friend = UserProfile.checkUser(friend)
		if user is None:
			return (None, friend, UserProfile.INVALID_USERNAME)
		if friend is None:
			return (user, None, UserProfile.INVALID_FRIEND_USERNAME)
		return (user, friend, UserProfile.SUCCESS)
		
	def accept(self, username, friend):
		user, friend, errCode = FriendRequest.verify(username, friend)
		if errCode != UserProfile.SUCCESS:
			return errCode
		req = getRequest(username, friend)
		if req == None:
			return UserProfile.REQUEST_DNE
		user.add_friend(self.friend)
		friend.add_friend(self.user)
		return UserProfile.SUCCESS		

	def decline(self, request):
		user, friend = self.authenticate(request)
		if user is not None and friend is not None:
			user.remove_friend(self.friend)
			friend.remove_friend(self.user)
			return {'errCode': SUCCESS}	
		return {'errCode': FAILURE}	

	def block(self, request):
		user, friend = self.authenticate(request)
		if user is not None and friend is not None:
			user.remove_friend(self.friend)
			friend.remove_friend(self.user)
			return {'errCode': SUCCESS}	
		return {'errCode': FAILURE}	
			

	def requestFriend(self, username, friend):
		user, friend_user, errCode = FriendRequest.verify(username, friend)
		if errCode != UserProfile.SUCCESS:
			return errCode
		check = FriendRequest.checkIfFriends(username,friend)
		if check != None:
			return UserProfile.ALREADY_FRIENDS
		req = FriendRequest.getRequest(username, friend)
		if req != None:
			return UserProfile.REQUEST_EXISTS
		newRequest = FriendRequest.objects.create(user=username, 
			friend=friend)
		newRequest.save()
		check = FriendRequest.getRequest(username, friend)
		return UserProfile.SUCCESS

	@classmethod
	def getRequest(self, username, friend):
		try:
			req = FriendRequest.objects.get(user=username, friend=friend)
		except FriendRequest.DoesNotExist as e:
			req = None
		return req

	@classmethod
	def checkIfFriends(self, username, friend):
		user, friend, errCode = FriendRequest.verify(username, friend)
		if errCode == UserProfile.SUCCESS:
			try:
				check = user.friends.get(username=friend)
			except UserProfile.DoesNotExist as e:
				check = None
			return check