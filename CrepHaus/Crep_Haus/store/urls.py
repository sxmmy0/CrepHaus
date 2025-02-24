from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage URL
    path('accounts/', include('allauth.urls')), # URL for allauth authentication
]
