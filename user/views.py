# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import SignupForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after signup
            return redirect('home')  # Redirect to home page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# accounts/views.py

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
# accounts/views.py


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout

def home(request):
    return render(request,'home.html')



@login_required
def profile_view(request):
    return render(request, 'profile.html')  # Create this template