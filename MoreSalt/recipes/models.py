from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=75)
    '''image =models.ImageField () might need pillow python -m pip install Pillow''' 
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title