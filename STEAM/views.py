from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf.urls import handler404
from django.urls import path, include
from django.contrib import admin

def about(request):
    return render(request, 'about.html')

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
 
handler404 = custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home')),  # Ensure this line exists
]