from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index),
    path('getAllData/', views.getAllData),
    path('getDetail/<int:id>/', views.getDetail),
    path('createDetail/', views.createDetail),
    path('deleteDetail/<int:id>/', views.deleteDetail),
    path('updateData/<int:id>/', views.updateData),
    path('register_user/', views.register_user),
    path('login_view/', obtain_auth_token)
]