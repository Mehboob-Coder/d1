from django.core import validators
from django import forms
from .models import *
class StudentForm(forms.ModelForm):
    # name= forms.CharField(max_length=10 ,required=False)
    class Meta:
        model = user
        
        fields = ['name','email','password']
        labels={'name':'Enter your name','email':'Enter your email','password':'Enter your password'}
        help_text={'name':'Enter your full name'}
        error_messages={'name':{'required':'name likhna ha'}}
        widgets = {'password':forms.PasswordInput, 
                   'name':forms.TextInput(attrs={'class':'my class', 'placeholder':'ya nahi likhna '})}
