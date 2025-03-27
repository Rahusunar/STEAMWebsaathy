from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.products,name='products'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('CodingClass/',views.coding_class_enrollment,name='CodingClass'),
    path('CodingClass/success/', views.success, name='success'),
    path('kits/',views.kits,name='kits'),
    
]