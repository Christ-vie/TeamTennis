from rest_framework import viewsets
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response

# Create your views here.


class PersonnelView(viewsets.ModelViewSet):
        queryset = Personnel.objects.all()
        serializer_class = PersonnelSerializer
class AbonnementView(viewsets.ModelViewSet):
        queryset = Abonnement.objects.all()
        serializer_class = AbonnementSerializer
class CompteView(viewsets.ModelViewSet):
        queryset = Compte.objects.all()
        serializer_class = CompteSerializer
class FactureView(viewsets.ModelViewSet):
        queryset = Facture.objects.all()
        serializer_class = FactureSerializer
class EntrepriseView(viewsets.ModelViewSet):
        queryset = Entreprise.objects.all()
        serializer_class = EntrepriseSerializer