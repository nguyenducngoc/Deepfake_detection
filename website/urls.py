"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from .views import index


app_name = 'website'


urlpatterns = [
    path('', index, name='home'),
    # path('about/', about, name='about'),
    # path('predict/', predict_page, name='predict'),
    # path('cuda_full/',cuda_full,name='cuda_full'),
]
