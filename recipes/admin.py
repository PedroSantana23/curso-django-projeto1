from django.contrib import admin
from .models import Category, Recipe
from unfold.admin import ModelAdmin

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(ModelAdmin):
    ...