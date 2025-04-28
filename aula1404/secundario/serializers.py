from rest_framework import serializers
from .models import Piloto, Carro
#piloto serializer
class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'
#carro serializer
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'
