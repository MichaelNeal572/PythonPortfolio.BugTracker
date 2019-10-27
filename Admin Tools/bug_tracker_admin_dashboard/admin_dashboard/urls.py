from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="dashboard-home")
    path('about/', views.about, name='dashboard-about')
]