"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import handler404

urlpatterns = [
    path("sessionUniversity/", include("sessionUniversity.urls")),
    path("car/", include("car.urls")),
    path('admin/', admin.site.urls),
    path('lecture1/', include('lect1.urls')),
    path('exams/', include('exams.urls')),
    path('shop/', include('shopping.urls')),
    path('z/', include('z.urls')), 
    path('', include("car.urls")),
]


handler404 = 'shopping.views.error_404_view'