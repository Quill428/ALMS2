from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Category, SubCategory, CustomerResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CustomerResponseForm, CreatePost

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
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('recipes:list')
    else:
        form = CreatePost()
    return render(request, 'recipes/recipe_new.html', { 'form': form})

def category_recipes(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    recipes = Recipe.objects.filter(categories=category)
    return render(request, 'recipe/category_recipes.html', {'category': category, 'recipes':recipes })

def subcategory_recipes(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id = subcategory_id)
    recipes = Recipe.objects.filter(subcategories=subcategory)
    return render(request, 'recipe/subcategory_recipes.html', {'subcategory': subcategory, 'recipes':recipes })

def submit_response(request):
    if request.method == 'POST':
        form = CustomerResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            if request.user.is_authenticated:
                response.user = request.user
            response.save()
            return redirect('/')
    else:
        form = CustomerResponseForm()

    return render(request, 'recipes/submit_response.html',  {'form': form})

def homepage(request):
    recent_responses = CustomerResponse.objects.order_by('-created_at')[:3]  # Get top 3 latest responses
    print("DEBUG: Recent Responses:", list(recent_responses)) #"Recent Responses:", recent_responses)
    return render(request, 'home.html', {'recent_responses': recent_responses}) #Home.html