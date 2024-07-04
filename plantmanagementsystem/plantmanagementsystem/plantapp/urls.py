from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('index/',views.index),
    path('viewplant/',views.viewplant,name='viewplant'),
    path('addplant/',views.addplant,name='addplant'),
    path('delete/<int:pk>',views.deleteplant,name='deleteplant'),
    path('edit/<int:pk>',views.editplant,name='editplant')
]
