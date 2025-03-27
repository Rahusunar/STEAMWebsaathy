from django.shortcuts import render,redirect, get_object_or_404
from .forms import CodingClassEnrollmentForm
from .models import exploreKits,Category,Product
# Create your views here.
def products(request):
    return render(request,'products.html')

def success(request):
    return render(request, 'success.html')


def coding_class_enrollment(request):
    if request.method == 'POST':
        form = CodingClassEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = CodingClassEnrollmentForm()
    
    return render(request, 'CodingClass.html', {'form': form})
def kits(request):
    expokit = exploreKits.objects.all()
    return render(request,'product.html',{'kit':expokit} )
    

def kit_details(request, explorekits_id):
    exkit = get_object_or_404(exploreKits, id=explorekits_id)
    return render(request, 'product.html', {'post': exkit})
    

      
def category_products(request,category_id):
    category = get_object_or_404(Category,category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'product.html', {'products': products, 'category': category})

