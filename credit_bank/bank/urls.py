from django.urls import path
from . import views

urlpatterns = [
    # Site
    path('', views.index, name='bank'),  # здесь мы переходим в функцию index в файле views
]
