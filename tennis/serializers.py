from rest_framework import serializers
from .models import *
class AbonnementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'
class PersonnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'
class CompteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compte
        fields = '__all__'
class EntrepriseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'
class FactureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'
