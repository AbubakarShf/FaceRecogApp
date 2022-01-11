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
# Create your views here.
class Register(APIView):
    RegisterSerializer_Class=RegisterSerializer
    def get(self,request):
        return render(request, 'register.html')
    def post(self,request,format=None):
        serializer=self.RegisterSerializer_Class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg={
                'msg':"Registered Successfully"
            }
            return render(request, 'index.html',msg)
        else:
            return Response({"Message":serializer.errors,"status":status.HTTP_400_BAD_REQUEST})
class Login(APIView):
    def get(self,request):
        return render(request, 'index.html')

    def post(self,request,format=None):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        response=redirect(reverse("CameraFormPage"))
        # response=render(request,'camera-form.html')
        return response
class CameraDetail(APIView):
    def get(self,request):
        return render(request,'Camera-Detail.html')
class CameraForm(APIView):
    def get(self,request):
        return render(request,'camera-form.html')
class SingleCamera(APIView):
    def get(self,request):
        return render(request,'Single-Camera.html')
class Logout(APIView):
    def get(self,request):
        pass