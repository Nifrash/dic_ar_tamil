from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WordViewSet, export_words_json

router = DefaultRouter()
router.register(r'words', WordViewSet, basename='words')

urlpatterns = [
    path('', include(router.urls)),
    path('export/json/', export_words_json, name='export_words_json'),
]