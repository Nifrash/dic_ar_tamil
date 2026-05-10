from django.urls import path
from . import views_dashboard

urlpatterns = [
    path('dashboard/', views_dashboard.user_dashboard, name='user_dashboard'),
    path('dashboard/add-word/', views_dashboard.add_word, name='add_word'),
]