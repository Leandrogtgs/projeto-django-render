from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('minha_pagina.urls')),  # Isso encaminha para as URLs da sua app
]
