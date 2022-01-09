
from django.contrib import admin
from django.urls import path
from .views import index,CameraDetail,CameraForm,SingleCamera


urlpatterns = [
    path('',index.as_view(),name="login"),
    path('details',CameraDetail.as_view(),name="Camera_Detail"),
    path('form',CameraForm.as_view(),name="Camera_Form"),
    path('camera',SingleCamera.as_view(),name="Single_Camera")

]
