# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from ..logreg.models import *
from .models import *

def flash_messages(request, errors):
	for error in errors:
		messages.error(request,error)

def home(request):
	user = User.objects.get(id = request.session['user_id'])
	# my_travel = User.travels.all()
	# other_travel = User.objects.exclude(id__in=my_travel).exclude(id=user.id)
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])
		users = User.objects.all()
		context = {
			'user': user,
			'users': users,
			# 'my_travel': my_travel,
			# 'other_travel': other_travel 
		}
		return render(request, 'travel/home.html', context)

def show(request, travel_id):
	context = {
		'travel': Travel.objects.get(id=travel_id),
	}
	return render(request, 'travel/show.html', context)

def add(request):
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])

	return render(request, 'travel/add.html')

def create(request):
	errors = Travel.objects.validate_travel(request.POST)
	if errors:
		flash_messages(request, errors)
		return redirect(reverse('new_travel'))
	else:
		travel = Travel.objects.create_travel(request.POST)
	return redirect(reverse('home'))



