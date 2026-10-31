from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=[
            'name',
            'email',
            'password',
            'branch',
            'cgpa',
            'graduation_year'
        ]
        widgets={
            'password':
            forms.PasswordInput(),
        }