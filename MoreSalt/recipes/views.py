from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

# Create your views here.
def recipes_list(request):
    recipes = Recipe.objects.all().order_by('-date')
    return render(request, 'recipes/recipes_list.html', {'recipes':recipes})

def recipe_page(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'recipes/recipe_page.html', {'recipe':recipe})

@login_required(login_url="/users/login/")
def recipe_new(request):
    return render(request, 'recipes/recipe_new.html')