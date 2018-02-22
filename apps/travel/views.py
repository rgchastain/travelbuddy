# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from ..logreg.models import User
from .models import Travel

def flash_messages(request, errors):
	for error in errors:
		messages.error(request,error)
	return errors
def home(request):
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])
		my_trips = user.travel_plans.all()
		other_trips = Travel.objects.exclude(plans__id=user.id)
		context = {
			# 'travel': Travel.objects.all(),
			'user': user,
			'my_trips': my_trips,
			'other_trips': other_trips
		}
		return render(request, 'travel/home.html', context)

def show(request, id):
	travel = Travel.objects.get(id=id)
	context = {
		'travel': Travel.objects.get(id=id),
		'others': travel.plans.all()
	}
	return render(request, 'travel/show.html', context)

def add_trip(request, id):
	user = User.objects.get(id = request.session['user_id'])
	travel = Travel.objects.get(id=id)

	travel.plans.add(user)

	return redirect(reverse('home'))

def add(request):
	if 'user_id' in request.session:

		return render(request, 'travel/add.html')

def create(request):
	errors = Travel.objects.validate_travel(request.POST)
	if errors:
		flash_messages(request, errors)
		return redirect(reverse('new_travel'))
	else:
		travel = Travel.objects.create_travel(request.POST, request.session['user_id'])
	return redirect(reverse('home'))



