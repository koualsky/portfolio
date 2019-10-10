from django.urls import path
from . import views

urlpatterns = [
    path('', views.work, name='work'),
    path('about/', views.about, name='about'),
]
