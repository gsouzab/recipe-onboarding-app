from rest_framework import serializers
from apps.recipes.models import Recipe, Ingredient

class IngredientsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Ingredient
    fields = ['name']

class RecipeSerializer(serializers.ModelSerializer):
  ingredients = IngredientsSerializer(many=True, allow_empty=False)
  class Meta:
    model = Recipe
    fields = ['id', 'name', 'description', 'ingredients']

  def _bulk_create_ingredients(self, recipe, ingredients_data):
    ingredients = []
    for ingredient_data in ingredients_data:
      ingredient = Ingredient(recipe=recipe, **ingredient_data)
      ingredients.append(ingredient)

    Ingredient.objects.bulk_create(ingredients)

  def create(self, validated_data):
    ingredients_data = validated_data.pop('ingredients')
    recipe = Recipe.objects.create(**validated_data)
    self._bulk_create_ingredients(recipe=recipe, ingredients_data=ingredients_data)
    
    return recipe
  
  def update(self, instance, validated_data):
    ingredients_data = validated_data.pop('ingredients', None)

    if ingredients_data is not None:
      instance.ingredients.all().delete()
      self._bulk_create_ingredients(recipe=instance, ingredients_data=ingredients_data)

    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    
    instance.save()
    return instance
