from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.shortcuts import get_object_or_404
from .models import Produit
from .serializers import ProduitSerializer


# ─── Liste + Création ─────────────────────────────────────────────────────────

class ProduitListCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]  # pour gérer les images

    def get(self, request):
        produits = Produit.objects.all().order_by('-date_creation')
        serializer = ProduitSerializer(produits, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ProduitSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ─── Détail + Modification + Suppression ──────────────────────────────────────

class ProduitDetailView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_object(self, pk):
        return get_object_or_404(Produit, pk=pk)

    def get(self, request, pk):
        produit = self.get_object(pk)
        serializer = ProduitSerializer(produit, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        produit = self.get_object(pk)
        serializer = ProduitSerializer(produit, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        produit = self.get_object(pk)
        serializer = ProduitSerializer(produit, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        produit = self.get_object(pk)
        produit.delete()
        return Response({"message": "Produit supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)