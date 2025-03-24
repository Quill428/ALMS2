from django import forms 
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title', 'author','banner', 'ingredients', 'body', 'slug']