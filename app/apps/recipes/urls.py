from django.urls import path
from apps.recipes import views

urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='list-recipes'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='detail-recipe'),
]
