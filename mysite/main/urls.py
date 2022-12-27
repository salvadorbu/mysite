from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contacts'),
    path('tanks/', views.tanks, name='tanks'),
    path('canvas/', views.canvas, name='canvas'),
]