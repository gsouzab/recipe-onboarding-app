from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.recipes.models import Recipe, Ingredient
from apps.recipes.serializers import RecipeSerializer

def create_recipe_with_ingredients(ingredients=[{'name': 'ingredient'}], **recipe_params):
  """Create and return a recipe."""
  default_recipe = {
    'name': 'Recipe name',
    'description': 'Recipe description',
  }

  default_recipe.update(recipe_params)
  recipe = Recipe.objects.create(**default_recipe)

  for ingredient in ingredients:
    Ingredient.objects.create(recipe=recipe, **ingredient)

  return recipe

class RecipeTestCase(APITestCase):

  def test_list_recipes(self):
    """
    Test listing recipes.
    """
    create_recipe_with_ingredients()
    create_recipe_with_ingredients()

    response = self.client.get('/recipes/')

    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, serializer.data)


  def test_create_recipe_missing_ingredients(self):
    """
    Test error when creating a recipe without ingredients.
    """
    data = {'name': 'pizza', 'description': 'put in the oven', 'ingredients': []}

    response = self.client.post('/recipes/', data, format='json')
    recipes = Recipe.objects.all()
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEquals(len(recipes), 0)

  def test_create_recipe_success(self):
    """
    Test saving a recipe.
    """
    data = {
      'name': 'toast',
      'description': 'add the stuff in the bread',
      'ingredients': [{'name': 'cheese'},{'name': 'bread'}, {'name': 'tomato'}, {'name': 'onion'}]
    }
    response = self.client.post('/recipes/', data, format='json')

    recipe = Recipe.objects.get(id=response.data['id'])
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    serialized_recipe = RecipeSerializer(recipe)
    self.assertEqual(response.data, serialized_recipe.data)

  def test_patch_recipe(self):
    """
    Test partially updating a recipe.
    """
    recipe = create_recipe_with_ingredients()
    data = {
      'name': 'updated recipe',
      'ingredients': [{'name': 'potato'}]
    }
    response = self.client.patch(reverse('detail-recipe', args=[recipe.id]), data, format='json')
    db_recipe = Recipe.objects.get(id=response.data['id'])

    serialized_recipe = RecipeSerializer(db_recipe)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, serialized_recipe.data)

  def test_delete_recipe(self):
    """
    Test deleting a recipe.
    """
    to_delete_recipe = create_recipe_with_ingredients()
    create_recipe_with_ingredients()
    
    response = self.client.delete(reverse('detail-recipe', args=[to_delete_recipe.id]), format='json')
    recipes = Recipe.objects.all()

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertFalse(Recipe.objects.filter(id=to_delete_recipe.id).exists())
    self.assertEqual(len(recipes), 1)
    