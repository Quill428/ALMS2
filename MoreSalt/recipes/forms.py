from django import forms 
from . import models
from .models import CustomerResponse

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title', 'author','banner', 'ingredients', 'body', 'slug']

class CustomerResponseForm(forms.ModelForm):
    class Meta:
        model = CustomerResponse
        fields = ['content']