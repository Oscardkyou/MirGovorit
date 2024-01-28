from django.shortcuts import render, redirect
from .models import Product, Recipe, RecipeProduct

def Product(request):
    product = Product.objects.all()
    return render(request, 'index.html')

def Recipe(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipes': recipes})

def RecipeProduct(request):
    recipe_products = RecipeProduct.objects.all()
    return render(request, 'recipe_product.html', {'recipe_products': recipe_products})
