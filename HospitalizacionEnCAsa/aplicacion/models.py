from django.db import models

class Entidad (models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)

class Historia (models.Model):
    id_historia=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    sexo=models.CharField(max_length=10)
    sugerencia_de_cuidado=models.CharField(max_length=250)

class Person (models.Model):
    id_per=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    cargo=models.CharField(max_length=30)
    sexo=models.CharField(max_length=10)
    correo=models.CharField(max_length=50)

class Paciente (models.Model):
    id_pax=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    celular=models.CharField(max_length=30)
    correo=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    fecha_nacimiento=models.DateTimeField(max_length=50)

class Familiar (models.Model):
    id_Fam=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    parentezco=models.CharField(max_length=30)
    identificacion=models.IntegerField()
    telefono=models.IntegerField()
    correo=models.CharField(max_length=50)

class Auxiliar (models.Model):
    id_aux=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    correo=models.CharField(max_length=50)

class vitales (models.Model):
    id=models.IntegerField(primary_key=True)
    id_pax=models.CharField(max_length=30)
    id_per=models.CharField(max_length=30)
    oximetria=models.CharField(max_length=20)
    frecuencia_respiratoria=models.CharField(max_length=20)
    frecuencia_cardiaca=models.CharField(max_length=50)
    temperatura=models.CharField(max_length=50)
    presion_arterial=models.CharField(max_length=50)
    glicemias=models.CharField(max_length=50)
    fecha_hora=models.DateTimeField(max_length=50)