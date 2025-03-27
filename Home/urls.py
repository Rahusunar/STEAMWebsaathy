from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home,name='home'),
    path('blogs_details/<int:blog_id>/', views.blogs_details, name='blogs_details'),
]