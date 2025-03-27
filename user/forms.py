# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Enter your email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Enter your username'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Create a password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Confirm your password'
        })
        self.fields['username'].help_text = 'Enter your desired username.'
        self.fields['password1'].help_text = 'Create a password of at least 6 characters.'
        self.fields['password2'].help_text = 'Confirm the password.'

    # Override password validation
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Passwords do not match!')

        if len(password1) < 6:
            raise forms.ValidationError('Your password must contain at least 6 characters.')

        return password2

    # Override the save method to include the email field
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']  # Save the custom email field
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'input-box',
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-box',
        'placeholder': 'Enter your password'
    }))
