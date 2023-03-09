from django.db import models

class Recipe(models.Model):
  """Recipe model"""
  name = models.CharField(max_length=255)
  description = models.TextField()


class Ingredient(models.Model):
  """Ingredient model"""
  name = models.CharField(max_length=255)
  recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
