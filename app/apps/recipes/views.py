from apps.recipes.models import Recipe
from apps.recipes.serializers import RecipeSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer
