from django.urls import path
from .views import ProduitListCreateView, ProduitDetailView, ProduitParCategorieView  # ← ajouter ici

urlpatterns = [
    path('produits/', ProduitListCreateView.as_view(), name='produit-list-create'),
    path('produits/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
    path('categories/<int:categorie_id>/produits/', ProduitParCategorieView.as_view(), name='produit-par-categorie'),  # ← bonus
]