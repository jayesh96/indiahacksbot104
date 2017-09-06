# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Hospital(models.Model):
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=200) 
	pincode = models.IntegerField()
	contact = models.IntegerField()
	beds = models.IntegerField()


	class Meta:
		ordering = ["-beds"]


	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return str(self.title)
