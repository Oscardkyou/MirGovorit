# MirGovoritBacken.cookbook.urls
from django.contrib import admin
from django.urls import path
from .views import Product, Recipe, RecipeProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', Product, name='product'),
    path('recipe/', Recipe, name='recipe'),
    path('recipeproduct/', RecipeProduct, name='recipeproduct'),
]
