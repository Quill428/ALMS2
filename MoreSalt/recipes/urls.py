from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('recipes_list', views.recipes_list, name="list"),
    path('new-recipe/', views.recipe_new, name="new_recipe"),
    path('recipe/<slug:recipe_slug>', views.recipe_page, name="page"),
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'),
    path('subcategory/<int:subcategory_id>/', views.subcategory_recipes, name='subcategory_recipes'),
    path('submit_response/', views.submit_response, name= 'submit_response')
]
