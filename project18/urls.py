"""
URL configuration for project18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app18.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',first,name='first'),
    path('second/',second,name='second'),
    path('thred/',thred,name='thred'),
    path('forth/',forth,name='forth'),
    path('five/',five,name='five'),
    path('six/',six,name='six'),
    path('seven/',seven,name='seven'),
    path('eight/',eight,name='eight'),
    path('nine/',nine,name='name'),
    path('ten/',ten,name='ten'),
    path('leven/',leven,name='leven')


]
