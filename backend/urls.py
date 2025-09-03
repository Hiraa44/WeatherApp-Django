from django.contrib import admin
from django.urls import path,include
from  . import views

urlpatterns = [
   path('home/', views.Get_Weather, name ='home'),
  # path('forms/', views.submitform, name='forms')
]