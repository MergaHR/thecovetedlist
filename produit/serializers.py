from rest_framework import serializers
from .models import Produit
from categorie.serializers import CategorieSerializer
from categorie.models import Categorie

class ProduitSerializer(serializers.ModelSerializer):
    image_produit = serializers.ImageField(required=False, allow_null=True)
    
    # Lecture : retourne l'objet catégorie complet
    categorie_detail = CategorieSerializer(source='categorie', read_only=True)
    
    # Écriture : accepte juste l'id
    categorie = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(),   # ← ajouter cet import
        allow_null=True,
        required=False
    )

    class Meta:
        model  = Produit
        fields = [
            'id',
            'categorie',          # pour écriture (POST/PUT/PATCH)
            'categorie_detail',   # pour lecture (GET)
            'nom_produit',
            'description',
            'prix',
            'quantite_stock',
            'image_produit',
            'date_creation',
            'date_modification',
        ]
        read_only_fields = ['date_creation', 'date_modification']