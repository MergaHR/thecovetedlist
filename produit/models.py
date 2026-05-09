from django.db import models
from categorie.models import Categorie

class Produit(models.Model):
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produits'
    )
    nom_produit = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_stock = models.IntegerField()
    image_produit = models.ImageField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_produit