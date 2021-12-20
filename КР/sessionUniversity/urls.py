from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exam/<exam_id>/', views.exam, name='exam'),
    path('forms/<d>/', views.forms, name="forms"),
    path('ex1/<id>/', views.ex1, name="ex1"),
    path('ex1/', views.ex1, name="ex1"),
    path('ex2/', views.ex2, name="ex2"),
    path('ex2/<id>/<date>/', views.ex2, name="ex2"),
    path('ex3/', views.ex3, name="ex3")

]