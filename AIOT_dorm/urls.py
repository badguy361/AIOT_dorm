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
from django.urls import path,include
# from dorm.views import post
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from dorm import views

router = DefaultRouter()
router.register('facilities1', views.FacilitiesViewSet1, basename='facilities1')
router.register('facilities2', views.FacilitiesViewSet2, basename='facilities2')
router.register('facilities3', views.FacilitiesViewSet3, basename='facilities3')
router.register('facilities4', views.FacilitiesViewSet4, basename='facilities4')
router.register('facilities5', views.FacilitiesViewSet5, basename='facilities5')

urlpatterns = [ 
    path('dorm/',include('dorm.urls')),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('',views.FacilitiesViewSet4.Home),
    # path('postdorm/', views.FacilitiesViewSet.post),
    # path('putdorm/', put),
    # path('dorm_class/',FacilitiesView.as_view()),
    # path('dorm_post/',FacilitiesView.post),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
