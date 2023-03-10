from apps.recipes.models import Recipe
from apps.recipes.serializers import RecipeSerializer
from rest_framework import generics

class RecipeList(generics.ListCreateAPIView):
  serializer_class = RecipeSerializer

  def get_queryset(self):
    queryset = Recipe.objects.all()
    name = self.request.query_params.get('name')
    if name is not None:
      queryset = queryset.filter(name__icontains=name)
    return queryset


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer
