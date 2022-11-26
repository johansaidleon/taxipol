from dataclasses import fields
from rest_framework import serializers
from .models import Auxiliar, Entidad, Familiar, Historia, Paciente, Person, vitales

class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Entidad
        fields='__all__'

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Historia
        fields='__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields='__all__'

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Familiar
        fields='__all__'

class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auxiliar
        fields='__all__'

class VitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=vitales
        fields='__all__'

