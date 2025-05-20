from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),  # <- adiciona a rota para a raiz do site
    path('pagina_inicial', views.pagina_inicial, name='pagina_inicial'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('adicionar-contatos/', views.adicionar_contatos, name='adicionar_contatos'),
    path('lista-contatos/', views.lista_contatos, name='lista_contatos'),
]
