from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from staff.models import MyUser


def user_login(request):
    """user login"""
    login_name = request.POST['username']
    password = request.POST['password']
    user = authenticate(login_name=login_name, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            HttpResponse("login successfully!")
        else:
            HttpResponse("invalid account")
    else:
        HttpResponse("invalid account")

def user_logout(request):
    """user logout"""
    logout(request)
    HttpResponse("logout successfully.")
