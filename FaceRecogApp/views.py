from cgitb import reset
import sqlite3
from django.shortcuts import render

from .models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from FaceRecogApp.camera import VideoCamera,LiveWebCam, get_cameras
# Create your views here.
GLOBAL_CURSOR=None

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
            messages.error(
                request, ("Email or Password is wrong, Try Again!"))
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def register_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        # Ensure password matches confirmation
        if password != confirmation:
            messages.error(request, 'Password must match!')
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.info(request, 'Username already taken.')
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
    data=get_cameras()
    return render(request, 'camera-form.html',context={'cameras':data})


@login_required(login_url='HomePage')
def SingleCamera(request):
    link=request.GET.get('link')
    return render(request, 'Single-Camera.html',context={'link':link})


@login_required(login_url='HomePage')
def Logout(request):
    logout(request)
    request.session.flush()
    request.session.clear_expired()

    return redirect(reverse("HomePage"))



from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse


@gzip.gzip_page
def Detection(request):
    try:
        link=request.GET.get('link')
        if(link=='0'):
            cam = VideoCamera()
        else:
            cam=LiveWebCam(link)
        return StreamingHttpResponse(getRecognizedVideo(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'app1.html')

@gzip.gzip_page
def LiveCamera(request):
    try:
        link=request.GET.get('link')
        if(link=='0'):
            cam=VideoCamera()
        else:
            cam = LiveWebCam(link)
        return StreamingHttpResponse(getVideo(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as ex:
        print(ex)
    return render(request, 'app1.html')
            
def getVideo(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def getRecognizedVideo(camera):
    while True:
        frame = camera.get_recognized_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')




       