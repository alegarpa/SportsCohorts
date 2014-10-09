from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserProfile(AbstractBaseUser):
	SUCCESS = 1
	USER_EXISTS = -1
	INVALID_USERNAME = -2
	INVALID_PASSWORD = -3
	INVALID_EMAIL = -4
	BAD_CREDENTIALS = -5
	DISABLED_ACCOUNT = -6
	MAX_USERNAME_LENGTH = 128
	MAX_PASSWORD_LENGTH = 128
	
	username = models.CharField(max_length=MAX_USERNAME_LENGTH)
	first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
	icon = models.ImageField(blank=True, null=True)
	friends = models.ManyToManyField('self', blank=True, null=True)
	
	objects = UserProfileManager()
	
	def __unicode__(self):
		return self.user.username
		
class UserProfileManager(BaseUserManager):

	def create_user(self, username, password, email):
		check = self.validate_user(username, password, email)
		if(check == User.SUCCESS):
			user, created = User.objects.get_or_create(username=username, password=password, email=email)
			if not created:
				return {'errCode': User.ERR_USER_EXISTS}
			else:
				user.save()
				profile = UserProfile(user=user)
				profile.save()
				return {'errCode': User.SUCCESS}
		return {'errCode': check}

	def validate_user(self, username, password, email):
		if username is None:
			return {'errCode': User.INVALID_USERNAME}
		elif email is None:
			return {'errCode': User.INVALID_EMAIL}
	
		if len(username) == 0 or len(username) > MAX_USERNAME_LENGTH:
			return {'errCode': User.INVALID_USERNAME}
		elif len(password) > MAX_PASSWORD_LENGTH:
			return {'errCode': User.INVALID_PASSWORD}

		f = forms.EmailField()
		try:
			email = f.clean(email)
		except forms.ValidationError as e:
			return {'errCode': User.INVALID_EMAIL}
			
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
			
class FriendRequest(models.Model):

	SUCCESS = 1
	FAILURE = -1
	
	FRIENDS = 1
	UNFRIENDED = 0
	BLOCKED = -1
		
	user = models.IntegerField()
	friend = models.IntegerField()
	status = models.IntegerField(default=UNFRIENDED)
	
	@login_required
	def authenticate(self, request):
		if request.user.id == self.user:
			if request.user.is_authenticated():
				try:
					user = UserProfile.objects.get(id=self.user)
					friend = UserProfile.objects.get(id=self.friend)
					return (user, friend)
				catch UserProfile.DoesNotExist as e:
					return (None, None)
		return (None, None)
		
	def accept(self, request):
		user, friend = self.authenticate(request)
		if user is not None and friend is not None:
			user.add_friend(self.friend)
			friend.add_friend(self.user)
			self.status = FRIENDS
			return {'errCode': SUCCESS}	
		return {'errCode': FAILURE}			

	def decline(self, request):
		user, friend = self.authenticate(request)
		if user is not None and friend is not None:
			user.remove_friend(self.friend)
			friend.remove_friend(self.user)
			self.status = UNFRIENDED
			return {'errCode': SUCCESS}	
		return {'errCode': FAILURE}	

	def block(self, request):
		user, friend = self.authenticate(request)
		if user is not None and friend is not None:
			user.remove_friend(self.friend)
			friend.remove_friend(self.user)
			self.status = BLOCKED
			return {'errCode': SUCCESS}	
		return {'errCode': FAILURE}	
			
	@classmethod
	def request(request, friend):
		if request.user.is_authenticated():
			try:
				friend = UserProfile.objects.get(id=self.friend)
				request = FriendRequest.objects.get_or_create(user=request.user.id, friend=friend.id)
				return {'errCode': SUCCESS}	
			except UserProfile.DoesNotExist as e:
				return {'errCode': User.FALURE}
			
			