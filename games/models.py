from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
	name = models.CharField()
	host = models.ForeignKey(User)
	sport = models.ForeignKey(Sport)
	time = models.DateTimeField()
	players = models.ManyToManyField(User)
	location = models.CharField()

	players_request = models.ManyToManyField(User)

	SUCCESS = 1
	INVALID_CREATOR = -1
	INVALID_NEW_PLAYER = -2
	GAME_DNE = -3
	INVALID_INVITER = -4
	INVALID_INVITEE = -5
	INVALID_PLAYER = -6
	INVALID_NEW_TIME = -7
	INVALID_LOCATION = -8

	def createGame(self, name, host, sport, time, location):
		try:
			h = User.objects.get(host)
		except User.DoesNotExist as e:
			return INVALID_CREATOR

		new_game = self.model(name = name, time = time, location=location)
		new_game.host = host
		new_game.sport = sport
		new_game.save()
		
		new_game.players.add(game)

		return SUCCESS

	def addPlayer(self, game, newPlayer):
		try:
			np = User.objects.get(newPlayer)
		except User.DoesNotExist as e:
			return INVALID_NEW_PLAYER

		game.players.add(newPlayer)
		return SUCCESS

	def invitePlayer(self, game, inviter, invitee):
		try:
			er = User.objects.get(inviter)
		except User.DoesNotExist as e:
			return INVALID_INVITER

		try:
			ee = User.objects.get(invitee)
		except User.DoesNotExist as e:
			return INVALID_INVITEE

		if inviter.game_set.filter(game).count() == 0:
			return INVALID_INVITER

		game.players_request.add(invitee)

		return SUCCESS

	def removePlayer(self, game, player):
		try:
			p = User.objects.get(player)
		except User.DoesNotExist as e:
			return INVALID_PLAYER

		if player.game_set.filter(game).count() == 0:
			return INVALID_PLAYER

		player.delete()

		return SUCCESS

	def gameTimeChange(self, game, newTime):
		game.time = newTime

		return SUCCESS

	def gameLocationChange(self, game, newLocation):
		if newLocation == "":
			return INVALID_LOCATION
		game.location = newLocation

		return SUCCESS

	def __unicode__(self):
		return self.name



class Sport(models.Model):
	name = models.CharField()

	SUCESS = 1


	#def addGame(game):
	#	if Sport.objects.filter(name = self.name).count() == 0:
	#		sport = Sport(name= self.name)
	#		sport.save()
	#		sport.game_set.add(game)
	#		return SUCESS
	#	else:

		
	def __unicode__(self):
		return self.name