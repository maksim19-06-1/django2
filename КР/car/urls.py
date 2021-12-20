from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ex1/<id>/', views.ex1, name="ex1"),
    path('ex1/', views.ex1, name="ex1"),
    path('ex2/', views.ex2, name="ex2"),

]