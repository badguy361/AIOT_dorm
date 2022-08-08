"""AIOT_dorm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('info1/', views.FacilitiesViewSet1.get, name='dorm'),
    # path('connect', views.FacilitiesViewSet4.connect, name='connect'),
    path('getJsondata1/', views.FacilitiesViewSet1.getJsondata, name='Jsondata'),

    path('info2/', views.FacilitiesViewSet2.get, name='dorm'),
    path('getJsondata2/', views.FacilitiesViewSet2.getJsondata, name='Jsondata'),

    path('info3/', views.FacilitiesViewSet3.get, name='dorm'),
    path('getJsondata3/', views.FacilitiesViewSet3.getJsondata, name='Jsondata'),

    path('info4/', views.FacilitiesViewSet4.get, name='dorm'),
    path('getJsondata4/', views.FacilitiesViewSet4.getJsondata, name='Jsondata'),
    path('Home/', views.FacilitiesViewSet4.Home, name='Home'),
    path('feedbacks/', views.FacilitiesViewSet4.feedbacks, name='dorm'),
    path('connect/', views.FacilitiesViewSet4.connect, name='dorm'),
    
    path('info5/', views.FacilitiesViewSet5.get, name='dorm'),
    path('getJsondata5/', views.FacilitiesViewSet5.getJsondata, name='Jsondata'),
]
