from django.shortcuts import render

# Create your views here.
def recipes_list(request):
    return render(request, 'recipes/recipes_list.html')