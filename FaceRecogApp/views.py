from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class index(APIView):
    def get(self,request):
        return render(request,'index.html')
class CameraDetail(APIView):
    def get(self,request):
        return render(request,'Camera-Detail.html')
class CameraForm(APIView):
    def get(self,request):
        return render(request,'camera-form.html')
class SingleCamera(APIView):
    def get(self,request):
        return render(request,'Single-Camera.html')