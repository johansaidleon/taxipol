from rest_framework import viewsets
from . import models
from . import serializers

class EntidadViewset(viewsets.ModelViewSet):
    queryset=models.Entidad.objects.all()
    serializer_class=serializers.EntidadSerializer

class HistoriaViewset(viewsets.ModelViewSet):
    queryset=models.Historia.objects.all()
    serializer_class=serializers.HistoriaSerializer    

class PersonViewset(viewsets.ModelViewSet):
    queryset=models.Person.objects.all()
    serializer_class=serializers.PersonSerializer 

class PacienteViewset(viewsets.ModelViewSet):
    queryset=models.Paciente.objects.all()
    serializer_class=serializers.PacienteSerializer 

class FamiliarViewset(viewsets.ModelViewSet):
    queryset=models.Familiar.objects.all()
    serializer_class=serializers.FamiliarSerializer

class AuxiliarViewset(viewsets.ModelViewSet):
    queryset=models.Auxiliar.objects.all()
    serializer_class=serializers.AuxiliarSerializer

class VitalesViewset(viewsets.ModelViewSet):
    queryset=models.vitales.objects.all()
    serializer_class=serializers.VitalesSerializer 

