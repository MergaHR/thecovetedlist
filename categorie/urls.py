from django.urls import path
from .views import CategorieListCreateView, CategorieRetrieveUpdateDestroyView

urlpatterns = [
    path('categories/', CategorieListCreateView.as_view(), name='categorie-list-create'),
    path('categories/<int:pk>/', CategorieRetrieveUpdateDestroyView.as_view(), name='categorie-detail'),
]