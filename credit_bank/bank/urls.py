from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bank'),  # здесь мы переходим в функцию index в файле views
    path('clients', views.clients, name='clients'),
    path('calculator', views.calculator, name='calculator'),
]
