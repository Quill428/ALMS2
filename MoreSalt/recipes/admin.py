from django.contrib import admin
from .models import Recipe,Category,SubCategory,CustomerResponse

# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Recipe)
admin.site.register(CustomerResponse)