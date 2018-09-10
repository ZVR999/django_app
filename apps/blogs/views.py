# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def home(request):
    return HttpResponse('HomePage')

def index(request):
    response = "Placeholder to list all blogs"
    return HttpResponse(response)

def new(request):
    response = 'Placeholder for a form to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, number):
    response = 'Placeholder to display '+str(number)
    return HttpResponse(response)

def edit(request, number):
    response = 'Placeholder to edit blog '+str(number)
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/blogs')
