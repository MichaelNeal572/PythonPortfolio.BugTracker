from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from . import views


urlpatterns = [
    path('', views.home, name="dashboard-home"),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='dashboard-about')
]