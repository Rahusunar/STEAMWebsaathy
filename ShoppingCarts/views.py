from django.shortcuts import render

# Create your views here.
def shoppingCart(request):
    return render(request, 'shoppingCart.html')