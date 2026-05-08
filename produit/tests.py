from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Produit


class ProduitAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.produit_data = {
            "nom_produit": "Laptop Dell XPS 15",
            "description": "Ordinateur portable 15 pouces",
            "prix": "899.99",
            "quantite_stock": 10
        }
        self.produit = Produit.objects.create(**self.produit_data)

    # ── GET Liste ────────────────────────────────────────────────────────
    def test_get_liste_produits(self):
        response = self.client.get(reverse('produit-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ── GET Détail ───────────────────────────────────────────────────────
    def test_get_detail_produit(self):
        response = self.client.get(reverse('produit-detail', args=[self.produit.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom_produit'], "Laptop Dell XPS 15")

    # ── POST Créer ───────────────────────────────────────────────────────
    def test_creer_produit(self):
        data = {
            "nom_produit": "iPhone 15 Pro",
            "description": "Smartphone Apple",
            "prix": "1199.99",
            "quantite_stock": 25
        }
        response = self.client.post(reverse('produit-list-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produit.objects.count(), 2)

    # ── PATCH Modifier ───────────────────────────────────────────────────
    def test_modifier_partiel_produit(self):
        response = self.client.patch(
            reverse('produit-detail', args=[self.produit.pk]),
            {"prix": "749.99"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['prix']), "749.99")

    # ── PUT Modifier complet ─────────────────────────────────────────────
    def test_modifier_complet_produit(self):
        data = {
            "nom_produit": "Laptop Dell Updated",
            "description": "Nouvelle description",
            "prix": "799.99",
            "quantite_stock": 5
        }
        response = self.client.put(
            reverse('produit-detail', args=[self.produit.pk]),
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom_produit'], "Laptop Dell Updated")

    # ── DELETE Supprimer ─────────────────────────────────────────────────
    def test_supprimer_produit(self):
        response = self.client.delete(reverse('produit-detail', args=[self.produit.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Produit.objects.count(), 0)

    # ── Produit inexistant ───────────────────────────────────────────────
    def test_produit_inexistant(self):
        response = self.client.get(reverse('produit-detail', args=[9999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)