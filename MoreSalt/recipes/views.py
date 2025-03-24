from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Category, SubCategory
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def recipes_list(request):
    recipes = Recipe.objects.all().order_by('-date')
    return render(request, 'recipes/recipes_list.html', {'recipes':recipes})

def recipe_page(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'recipes/recipe_page.html', {'recipe':recipe})

@login_required(login_url="/users/login/")
def recipe_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save with user
            return redirect('recipes:list')
    else:
        form = forms.CreatePost()
    return render(request, 'recipes/recipe_new.html', { 'form': form})

def category_recipes(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    recipes = Recipe.objects.filter(categories=category)
    return render(request, 'recipe/category_recipes.html', {'category': category, 'recipes':recipes })

def subcategory_recipes(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id = subcategory_id)
    recipes = Recipe.objects.filter(subcategories=subcategory)
    return render(request, 'recipe/subcategory_recipes.html', {'subcategory': subcategory, 'recipes':recipes })