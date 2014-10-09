from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
	name = models.CharField()
	host = models.ForeignKey(User)
	sport = ()
	time = models.DateTimeField()
	players = models.ManyToManyField(User)

class Sport(models.Model):
	name = models.CharField()
	games = models.ManyToManyField(Game)