# Generated by Django 4.1.1 on 2022-10-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id_aux', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id_Fam', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('parentezco', models.CharField(max_length=30)),
                ('identificacion', models.IntegerField(max_length=20)),
                ('telefono', models.IntegerField(max_length=20)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id_historia', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField(max_length=30)),
                ('sexo', models.CharField(max_length=10)),
                ('sugerencia_de_cuidado', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_pax', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateTimeField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id_per', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('cargo', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='vitales',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_pax', models.CharField(max_length=30)),
                ('id_per', models.CharField(max_length=30)),
                ('oximetria', models.CharField(max_length=20)),
                ('frecuencia_respiratoria', models.CharField(max_length=20)),
                ('frecuencia_cardiaca', models.CharField(max_length=50)),
                ('temperatura', models.CharField(max_length=50)),
                ('presion_arterial', models.CharField(max_length=50)),
                ('glicemias', models.CharField(max_length=50)),
                ('fecha_hora', models.DateTimeField(max_length=50)),
            ],
        ),
    ]