from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='Übersicht'),
    path('impressum/', views.impressum, name='Impressum'),
    path('new/', views.new, name='New'),
    path('edit/', views.edit, name='Edit'),
    path('', views.index, name='Index'),
]