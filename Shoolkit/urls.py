from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.schoolkits,name='schoolkits'),
    # path('add_to_cart/',views.cart,name='add_to_cart'),
    path('kitinfo/<int:id>/', views.kitinfo, name='kitinfo'),
    
]