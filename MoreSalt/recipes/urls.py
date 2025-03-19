from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes_list, name="list"),
    path('new-recipe/', views.recipe_new, name="new_recipe"),
    path('<slug:slug>', views.recipe_page, name="page"),
]
