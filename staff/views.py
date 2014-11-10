from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from staff.models import MyUser


