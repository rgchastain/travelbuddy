# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
	def validate_registration(self, form_data):
		errors = []

		if len(form_data['name']) < 3:
			errors.append('Name must be greater than 3 characters.')
		if len(form_data['username']) < 3:
			errors.append('Username must be greater than 3 characters.')
		if len(form_data['password']) < 8:
			errors.append('Password must be 8 characters long.')
		if form_data['password'] != form_data['password_confirmation']:
			errors.append('Passwords must match.')
		
		return errors

	def validate_login(self, form_data):
		errors = []
        # check DB for post_data['username']
		if len(self.filter(username=form_data['username'])) > 0:
			user = self.filter(username=form_data['username'])[0]
			if not bcrypt.checkpw(form_data['password'].encode(), user.password.encode()):
				errors.append('username/password incorrect')
		else:
			errors.append('username/password incorrect')

		if errors:
			return errors

		return user
	
	def create_user(self, form_data):
		hashedpw = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())

		return User.objects.create(
			name = form_data['name'],
			username = form_data['username'],
			password = hashedpw,
		)


class User(models.Model):
	name = models.CharField(max_length = 50)
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()

