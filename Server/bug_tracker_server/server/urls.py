from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'server-home')
    path('create-tables/', views.create_tables, name = 'server-create-tables')
]