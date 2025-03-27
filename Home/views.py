from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import blogs
# Create your views here.
def home(request):
    blog = blogs.objects.all()
    return render(request, 'Home/home.html', {'blog': blog})
def blogs_details(request, blog_id):
    blog = get_object_or_404(blogs, id=blog_id)
    return render(request, 'blogs.html', {'post': blog})
    
    

