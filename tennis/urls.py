from django.urls import path, include
from rest_framework import routers
from tennis import views

router = routers.DefaultRouter()
router.register('personnels', views.PersonnelView)
router.register('abonnements', views.AbonnementView)
router.register('entreprises', views.EntrepriseView)
router.register('factures', views.FactureView)
router.register('comptes', views.CompteView)

urlpatterns = [
    path('', include(router.urls))
]
