from django.db import models


# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Abonnement(models.Model):

        dateDebut_abonnement = models.DateTimeField(auto_now_add=True)
        montant_abonnement = models.DecimalField(max_digits=5, decimal_places=2)
        dateRenouvellement_abonnement = models.DateTimeField(auto_now_add=False)
        modeDePaiement = models.CharField(max_length=250)
        def __str__(self):
            return self.montant_abonnement

class Compte(models.Model):
    id_abonnement = models.ForeignKey(Abonnement, on_delete=models.CASCADE)
    id_compte = models.AutoField(primary_key=True)
    nom_compte = models.CharField(max_length=250, editable=False)
    prenom_compte = models.CharField(max_length=250)
    sexe_compte = models.CharField(max_length=1)
    tel_compte = PhoneNumberField(default=None)
    email_compte = models.EmailField(max_length=250)
    datedeNaissance = models.DateField()

    def __str__(self):
        return self.nom_compte + ' _ ' + self.prenom_compte

class Entreprise(models.Model):
    id_entreprise = models.AutoField(primary_key=True)
    nom_entreprise = models.CharField(max_length=250)
    code_postal_entreprise = models.CharField("ZIP / Postal code", max_length=12)
    adresse_entreprise = models.CharField(max_length=250)
    tel_entreprise = PhoneNumberField(default=None)

    def __str__(self):
        return self.nom_entreprise + ' _ ' + self.tel_entreprise
class Facture(Abonnement, Compte, Entreprise):

    date_facture = models.DateTimeField(auto_now_add=True)
    reference_facture = models.CharField(max_length=250)

class Personnel(models.Model):
    SEX = [
        ("M", "Male"),
        ("F", "Female")
    ]
    nom_personnel = models.CharField(max_length=250)
    prenom_personnel = models.CharField(max_length=250)
    sex_personnel = models.CharField(max_length=1, choices=SEX)
    tel_personnel = PhoneNumberField(default=None)
    email_personnel = models.EmailField(max_length=250)
    dateDeNaissance_personnel = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.nom_personnel + ' _ ' + self.prenom_personnel