from django import forms
from .models import CodingClassEnrollment

class CodingClassEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CodingClassEnrollment
        fields = ['name', 'mobile', 'course_level']
        