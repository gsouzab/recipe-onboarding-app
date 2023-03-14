from django.db import models

class Recipe(models.Model):
  """Recipe model"""
  name = models.TextField()
  description = models.TextField()

class Ingredient(models.Model):
  """Ingredient model"""
  name = models.TextField()
  recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
