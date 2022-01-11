from django.urls import path
from .views import Login,Register,Logout,CameraDetail,CameraForm,SingleCamera


urlpatterns = [
    path('',Login.as_view(),name="HomePage"),
    path('login',Login.as_view(),name="LoginPage"),
    path('register',Register.as_view(),name="RegisterPage"),
    path('logout',Logout.as_view(),name="LogoutPage"),
    path('details',CameraDetail.as_view(),name="CameraDetailPage"),
    path('form',CameraForm.as_view(),name="CameraFormPage"),
    path('camera',SingleCamera.as_view(),name="SingleCameraPage")

]
