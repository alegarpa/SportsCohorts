from django.db import models

class messagePost(models.Model):
	MAX_COMMENT_LENGTH = 500

	text = models.CharField(max_length = MAX_COMMENT_LENGTH)
