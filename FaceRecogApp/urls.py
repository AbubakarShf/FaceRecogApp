from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_user, name="HomePage"),
    path('login', views.login_user, name="LoginPage"),
    path('register', views.register_user, name="RegisterPage"),
    path('logout', views.Logout, name="LogoutPage"),
    path('details', views.CameraDetail, name="CameraDetailPage"),
    path('form', views.CameraForm, name="CameraFormPage"),
    path('camera', views.SingleCamera, name="SingleCameraPage"),
    path('live', views.Detection, name="live"),
    path('weblive', views.LiveCamera, name="weblive"),
    path('label', views.label, name="label"),
    path('updateUser', views.updateUser, name="update"),

]
