from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

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
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(SubCategory, related_name="posts", blank=True)
    banner = models.ImageField(upload_to='media', default='fallback.png', blank=True)
    description= models.TextField(default='description')
    brief_description=models.CharField(max_length=600)
    ingredients = models.TextField(default='ingredients:')
    body = models.TextField(default='Directions')
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Auto-generate slug from title before saving"""
        if not self.slug:  # Only generate if slug is not already set
            self.slug = slugify(self.title)  # Converts spaces to dashes

        if not self.brief_description:
            if len(self.description) > 600:
                self.brief_description = self.description[:600]
            else:
                self.brief_description = self.description

        super().save(*args, **kwargs)
    
#recipe name, image, author, ingredients, cooking directions, category, and subcategory.
    def __str__(self):
        return self.title
    
class CustomerResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank =True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Response from {self.user.username if self.user else "Anonymous"}'
    
    class Meta:
        ordering=['-created_at']