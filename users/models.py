from django.db import models

class User(models.Model):
	MAX_NAME_LENGTH = 30

	name = models.CharField(max_length = MAX_NAME_LENGTH)
