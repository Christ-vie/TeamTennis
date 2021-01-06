from django.urls import path, include
from rest_framework import routers
from tennis import views

router = routers.DefaultRouter()
router.register('personnels', views.PersonnelView)
router.register('abonnements', views.AbonnementView)

urlpatterns = [
    path('', include(router.urls))
]
