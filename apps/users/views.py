# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Placeholder for users to create a new user record')

def login(request):
    return HttpResponse('Placeholder for user to login')

def users(request):
    return HttpResponse('Placeholder to later display all the list of users')