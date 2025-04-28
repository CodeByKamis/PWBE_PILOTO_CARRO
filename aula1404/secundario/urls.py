from django.urls import path
from .views import PilotoListCreateAPIView, CarroListCreateAPIView, PilotoRetrieveUpdateDestroyAPIView, CarroRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('piloto/', view= PilotoListCreateAPIView.as_view()), #para ver o piloto
    path('carro/', view= CarroListCreateAPIView.as_view()), #para ver o carro
    path('piloto/<int:pk>/', view= PilotoRetrieveUpdateDestroyAPIView.as_view()),#PilotoRetrieveUpdateDestroyAPIView -> nele é possível consultar, deletar e atualizar
    path('carro/<int:pk>/', view= CarroRetrieveUpdateDestroyAPIView.as_view()),#CarroRetrieveUpdateDestroyAPIView -> nele é possível consultar, deletar e atualizar




]