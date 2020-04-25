from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('pollster/', views.index, name='home'),
    path('pollster/<str:pk>/detail/', views.detail, name='detail'),
    path('pollster/<str:pk>/results/', views.results, name='results'),
    path('pollster/<str:pk>/vote/', views.vote, name='vote'),
    path('resultsdata/<str:obj>/', views.resultsData, name='resultsdata'),
]
