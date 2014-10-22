from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def loginsuccess(request):
    """if user login successfully"""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return True
        else:
            return HttpResponse('invalid username or passwword')
