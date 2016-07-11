from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class token(models.Model):
	'''Model to hold token'''
	access_token = models.CharField(max_length = 20, blank=True)
	refresh_token  = models.CharField(max_length=20, blank=True)
	expire_timestamp = models.DateTimeField(blank = True)

	token_type = models.CharField(max_length=20, default = 'None')
	scope = models.TextField(blank=True)

	def has_expired(self):
		now = timezone.now()
		return  self.expire_timestamp <= now


	def __str__(self):
		return self.access_token

