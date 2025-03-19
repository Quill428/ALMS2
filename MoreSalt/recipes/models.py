from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Recipe(models.Model):
    title = models.CharField(max_length=75)
    author = models.CharField(max_length=75, default='Unknown_User')
    category = models.ForeignKey(Category, default='1', on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(SubCategory, related_name="posts", blank=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    ingredients = models.TextField(default='ingredients:')
    body = models.TextField(default='Directions')
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Auto-generate slug from title before saving"""
        if not self.slug:  # Only generate if slug is not already set
            self.slug = slugify(self.title)  # Converts spaces to dashes
        super().save(*args, **kwargs)
#recipe name, image, author, ingredients, cooking directions, category, and subcategory.
    def __str__(self):
        return self.title
    
