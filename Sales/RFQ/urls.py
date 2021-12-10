
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/detalles/<int:pk>',views.details, name='Details'),
]
