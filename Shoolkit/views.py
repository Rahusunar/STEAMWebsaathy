from django.shortcuts import render, get_object_or_404
from .models import kit

# Create your views here.
def schoolkits(request):
    kits = kit.objects.all()  # Get all kit objects
    return render(request, 'schoolkits.html', {'kits': kits})


def kitinfo(request, id):
    product = get_object_or_404(kit, id=id)  # Get the product by ID
    return render(request, 'kitinfo.html', {'product': product})

def cart(request):
    return render(request,'cart.html')