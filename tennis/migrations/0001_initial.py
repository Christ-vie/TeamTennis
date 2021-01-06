# Generated by Django 3.0.5 on 2021-01-03 14:48

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebut_abonnement', models.DateTimeField(auto_now_add=True)),
                ('montant_abonnement', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dateRenouvellement_abonnement', models.DateTimeField()),
                ('modeDePaiement', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id_compte', models.AutoField(primary_key=True, serialize=False)),
                ('nom_compte', models.CharField(editable=False, max_length=250)),
                ('prenom_compte', models.CharField(max_length=250)),
                ('sexe_compte', models.CharField(max_length=1)),
                ('tel_compte', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None)),
                ('email_compte', models.EmailField(max_length=250)),
                ('datedeNaissance', models.DateTimeField()),
                ('id_abonnement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tennis.Abonnement')),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id_entreprise', models.AutoField(primary_key=True, serialize=False)),
                ('nom_entreprise', models.CharField(max_length=250)),
                ('code_postal_entreprise', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('adresse_entreprise', models.CharField(max_length=250)),
                ('tel_entreprise', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_personnel', models.CharField(max_length=250)),
                ('prenom_personnel', models.CharField(max_length=250)),
                ('sex_personnel', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('tel_personnel', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None)),
                ('email_personnel', models.EmailField(max_length=250)),
                ('dateDeNaissance_personnel', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('entreprise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tennis.Entreprise')),
                ('compte_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tennis.Compte')),
                ('abonnement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tennis.Abonnement')),
                ('date_facture', models.DateTimeField(auto_now_add=True)),
                ('reference_facture', models.CharField(max_length=250)),
            ],
            bases=('tennis.abonnement', 'tennis.compte', 'tennis.entreprise'),
        ),
    ]