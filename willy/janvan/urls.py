from django.urls import path
from . import views

#define path

urlpatterns = [
    path('', views.mbilinyi, name = 'mbilinyi')
]

