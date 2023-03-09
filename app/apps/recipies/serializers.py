from rest_framework import serializers
from apps.recipies.models import Recipe, Ingredient

class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = ['name', 'description', 'ingredients']
