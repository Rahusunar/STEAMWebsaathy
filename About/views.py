from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect

def about(request):
    return render(request,'about.html')