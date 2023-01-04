from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='clipshare-home'),
    path('about/', views.about, name='clipshare-about'),
]