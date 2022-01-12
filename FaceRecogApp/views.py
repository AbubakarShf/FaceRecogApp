from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def login_user(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("CameraFormPage"))
        else:
            messages.success(
                request, ("Email or Password is wrong, Try Again!"))
            return render(request, 'index.html', {})
    else:
        return render(request, 'index.html')


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("CameraFormPage"))
    else:
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
