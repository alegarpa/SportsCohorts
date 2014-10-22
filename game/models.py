from django.db import models
import datetime
from users.models import User
from sport.models import Sport


class Game(models.Model):
	MAX_NAME_LENGTH = 30

	name = models.CharField(max_length=MAX_NAME_LENGTH)
	host = models.ForeignKey(User, related_name='gameHost')
	sport = models.ForeignKey(Sport)
	time = models.DateTimeField(default=datetime.now)
	players = models.ManyToManyField(User, related_name = 'gamePlayers')
	location = models.CharField(max_length = MAX_NAME_LENGTH)

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
			h = User.objects.get(username = name)
		except User.DoesNotExist as e:
			return INVALID_CREATOR

		try:
			sport_obj = Sport.objects.get(name = sport)
		except Sport.DoesNotExist as e:
			sport_obj = Sport.objects.create(name = sport)

		time_obj = datetime.strptime(time, "%Y-%m-%d %H:%M")
		new_game = self.model(name = name, time = time_obj, location=location)
		new_game.host = h
		new_game.sport = sport_obj
		new_game.save()
		
		new_game.players.add(h)

		return SUCCESS

	def addPlayer(self, game, newPlayer):
		try:
			np = User.objects.get(username = newPlayer)
		except User.DoesNotExist as e:
			return INVALID_NEW_PLAYER

		game_obj = Game.objects.get(name = game)

		game_obj.players.add(np)

		return SUCCESS

	def invitePlayer(self, game, inviter, invitee):
		try:
			inviter_obj = User.objects.get(name = inviter)
		except User.DoesNotExist as e:
			return INVALID_INVITER

		try:
			invitee_obj = User.objects.get(name = invitee)
		except User.DoesNotExist as e:
			return INVALID_INVITEE

		game_obj = Game.objects.get(name = game)

		if inviter_obj.game_set.filter(game_obj).count() == 0:
			return INVALID_INVITER

		game_obj.players_request.add(invitee)

		return SUCCESS

	def removePlayer(self, game, player):
		try:
			p = User.objects.get(name = player)
		except User.DoesNotExist as e:
			return INVALID_PLAYER

		game_obj = Game.objects.get(name = game)

		if p.game_set.filter(game_obj).count() == 0:
			return INVALID_PLAYER

		p.delete()

		return SUCCESS

	def gameTimeChange(self, game, newTime):
		game_obj = Game.objects.get(name = game)
		time_obj = datetime.strptime(newTime, "%Y-%m-%d %H:%M")

		game_obj.time = time_obj

		game_obj.save()

		return SUCCESS

	def gameLocationChange(self, game, newLocation):
		if newLocation == "":
			return INVALID_LOCATION

		game_obj = Game.objects.get(name = game)
		game_obj.location = newLocation
		game_obj.save()

		return SUCCESS

	def __unicode__(self):
		return self.name