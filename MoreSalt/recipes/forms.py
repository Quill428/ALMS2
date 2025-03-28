from django import forms 
from . import models
from .models import CustomerResponse, Recipe

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title','category', 'subcategories','banner','description','brief_description', 'ingredients', 'body']


    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user and not instance.pk:  # Only set author if the instance is new
            instance.author = user
        if commit:
            instance.save()
        return instance

class CustomerResponseForm(forms.ModelForm):
    class Meta:
        model = CustomerResponse
        fields = ['title', 'content']