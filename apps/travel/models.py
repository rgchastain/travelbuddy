# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..logreg import *
from django.db import models

class TravelManager(models.Manager):
	def validate_travel(self, form_data):
		errors = []
		if len(form_data['destination']) < 1:
			errors.append('Destination field cannot be empty.')
		if len(form_data['description']) < 1:
			errors.append('Description field cannot be empty.')
		if form_data['travel_from'] > form_data['travel_to']:
			errors.append('Date must be in the future.')

	def create_travel(self, new_data):
		return Travel.objects.create(
			destination = new_data['destination'],
			description = new_data['description'],
			travel_from = new_data['travel_from'],
			travel_to = new_data['travel_to']

		)
		


class Travel(models.Model):
	destination = models.TextField()
	description = models.TextField()
	travel_from = models.DateField()
	travel_to = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = TravelManager()

 