from django.db import models
from users.models import User
from sport.models import Sport

class Game(models.Model):
	MAX_NAME_LENGTH = 30

	name = models.CharField(max_length=MAX_NAME_LENGTH)
	#host = models.ForeignKey(User, related_name='gameHost')
	sport = models.CharField(max_length = MAX_NAME_LENGTH)
	#time = models.DateTimeField()
	location = models.CharField(max_length = MAX_NAME_LENGTH)
	#players = models.ManyToManyField(User, related_name='gamePlayers')