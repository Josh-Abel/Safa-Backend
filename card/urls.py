from webbrowser import get
from .views import CardViewSet, random_card, get_possibilities
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('cards', CardViewSet, basename='cards')

urlpatterns = [
    path('', include(router.urls)),
    path('cards/random', random_card, name='random_card'),
    path('cards/get_possibilities/<str:word>/',
         get_possibilities, name='get_possibilities'),
]
