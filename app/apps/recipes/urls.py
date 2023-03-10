from django.urls import path
from apps.recipes import views

urlpatterns = [
    path('recipes/', views.SnippetList.as_view(), name='list-recipes'),
    path('recipes/<int:pk>/', views.SnippetDetail.as_view(), name='detail-recipe'),
]
