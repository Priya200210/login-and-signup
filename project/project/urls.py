"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from login import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'market', views.MarketApi, basename = 'market')

# router.register(r'bedroomdata', views.BedroomDataApi, basename = 'bedroomdata')

urlpatterns = [
    path("",include('login.urls')),
    path('admin/', admin.site.urls),
    path('signin/',views.Signin),
    path('signup/',views.Signup),
    path('pages/',views.pages_list),
    path('pagesview/<int:page_id>/',views.list_pages),
    path('pagescreate/',views.create_page),
    path('student/',views.student),
    path("students/",views.student_view),
    path("studentlist/<int:student_id>/",views.student_object),
    path("studentcreate/",views.student_create),
    
    
]
