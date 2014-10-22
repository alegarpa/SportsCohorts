from django.db import models
#from Game.models import Game


class Sport(models.Model):
	MAX_NAME_LENGTH = 30

	name = models.CharField(max_length = MAX_NAME_LENGTH)
	#games = models.ManyToManyField(Game)

	#def addGame(game):
	#	if Sport.objects.filter(name = self.name).count() == 0:
	#		sport = Sport(name= self.name)
	#		sport.save()
	#		sport.game_set.add(game)
	#		return SUCESS
	#	else:

		
	def __unicode__(self):
		return self.name