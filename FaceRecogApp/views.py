from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.shortcuts import render, redirect
from rest_framework.exceptions import AuthenticationFailed
from django.urls import reverse
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.


def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'camera-form.html')
        else:
            messages.success(request, "Email or Password is wrong, Try Again!")
            return render(request, 'index.html', {{messages}})
    else:
        return render(request, 'index.html')


def register_user(request):
    return render(request, "register.html")


@login_required(login_url='HomePage')
def CameraDetail(request):
    return render(request, 'Camera-Detail.html')


@login_required(login_url='HomePage')
def CameraForm(request):
    return render(request, 'camera-form.html')


@login_required(login_url='HomePage')
def SingleCamera(request):
    return render(request, 'Single-Camera.html')


@login_required(login_url='HomePage')
def Logout(request):
    logout(request)
    return redirect(reverse("HomePage"))
