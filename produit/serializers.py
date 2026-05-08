from rest_framework import serializers
from .models import Produit


class ProduitSerializer(serializers.ModelSerializer):
    image_produit = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model  = Produit
        fields = '__all__'
        read_only_fields = ['date_creation', 'date_modification']