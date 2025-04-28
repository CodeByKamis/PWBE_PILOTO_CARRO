from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Piloto, Carro
from .serializers import PilotoSerializer, CarroSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
#-------------------------------------------------------------------------------------------------------------------------

#PILOT

#quantas paginas e quantos por pagina
class PilotoPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class PilotoListCreateAPIView(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

    #esse schema serve para listar todos os pilotos
    @swagger_auto_schema(
            operation_description='List all pilots',
            responses={
                200: PilotoSerializer(many=True),
                400: 'Error'
            },
            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description = 'filter for name at pilot',
                    type=openapi.TYPE_STRING #MAIUSCULO SIGNIFICA QUE É UMA CONSTANTE
                )    
            ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    #esse de baixo serve para POST
    @swagger_auto_schema(
            operation_description='Creat new pilot',
            request_body=PilotoSerializer,
            responses={
                201: PilotoSerializer,
                400: 'Error'
            }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    #limita a classificação dependendo da equipe
    def perform_create(self, serializer):
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao']<= 5:
            raise serializers.ValidationError('Somente a DS16 deve ficar entre os 5')#limita as 5 posições apenas para quem for da ds16
        serializer.save()


# PILOTO -> consultar, atulizar e deletar
class PilotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk'

    #descrição para o get
    @swagger_auto_schema(
            operation_description='get the pilot for ID',
            responses={
                200: PilotoSerializer,
                404: 'Not Found',
                400: 'Error'
            }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    #descrição para o delete
    @swagger_auto_schema(
            operation_description='delete the pilot for ID',
            responses={
                200: PilotoSerializer,
                404: 'Not Found',
                400: 'Error'
            }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    #descrição para o put
    @swagger_auto_schema(
            operation_description='put the pilot for ID',
            request_body=PilotoSerializer,
            responses={
                200: PilotoSerializer,
                404: 'Not Found',
                400: 'Error'
            }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    #descrição para o patch
    @swagger_auto_schema(
            operation_description='patch the pilot for ID',
            request_body=PilotoSerializer,
            responses={
                200: PilotoSerializer,
                404: 'Not Found',
                400: 'Error'
            }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    #delete, put, puth

#---------------------------------------------------------------------------------------------------------------

#CAR
#quantas paginas e quantos por pagina
class CarroPaginacao(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5

class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPaginacao

    #esse schema serve para listar todos os carros
    @swagger_auto_schema(
            operation_description='List all cars',
            responses={
                200: CarroSerializer(many=True),
                400: 'Error'
            },
            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description = 'filter for name at car',
                    type=openapi.TYPE_STRING #MAIUSCULO SIGNIFICA QUE É UMA CONSTANTE
                )
                    
            ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

      #esse de baixo serve para POST
    @swagger_auto_schema(
            operation_description='Creat new car',
            request_body=CarroSerializer,
            responses={
                201: CarroSerializer,
                400: 'Error'
            }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    #limita a cor dependendo do nome
    def perform_create(self, serializer):
        if serializer.validated_data['nome'] != 'Kamila' and serializer.validated_data['cor']== 'Rosa':
            raise serializers.ValidationError('Somente a Kamila deve ficar com a cor Rosa') #limita para ser usada apemas por alguém com o nome Kamila 
        serializer.save()

# CARRO -> consultar, atulizar e deletar
class CarroRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    lookup_field = 'pk'

    
    #descrição para o get
    @swagger_auto_schema(
            operation_description='get the car for ID',
            responses={
                200: CarroSerializer,
                404: 'Not Found',
                400: 'Error'
            }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    #descrição para o delete
    @swagger_auto_schema(
            operation_description='delete the car for ID',
            responses={
                200: CarroSerializer,
                404: 'Not Found',
                400: 'Error'
            }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    #descrição para o put
    @swagger_auto_schema(
            operation_description='put the car for ID',
            request_body=CarroSerializer,
            responses={
                200: CarroSerializer,
                404: 'Not Found',
                400: 'Error'
            }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    #descrição para o patch
    @swagger_auto_schema(
            operation_description='patch the car for ID',
            request_body=CarroSerializer,
            responses={
                200: CarroSerializer,
                404: 'Not Found',
                400: 'Error'
            }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)