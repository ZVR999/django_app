# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Placeholder to display all the surverys created')

def new(request):
    return HttpResponse('Placeholder for user to add a new survey')