from django.db import models
#from Game.models import Game


class Sport(models.Model):
	MAX_NAME_LENGTH = 30

	name = models.CharField(max_length = MAX_NAME_LENGTH)
	#games = models.ManyToManyField(Game)