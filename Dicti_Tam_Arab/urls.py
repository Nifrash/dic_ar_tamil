from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('dictionary.urls')),

    path('', include('dictionary.dashboard_urls')),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]