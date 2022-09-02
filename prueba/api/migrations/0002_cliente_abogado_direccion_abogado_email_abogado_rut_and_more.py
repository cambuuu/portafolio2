# Generated by Django 4.1 on 2022-09-01 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_c', models.CharField(default='', max_length=20)),
                ('fono_c', models.CharField(default='', max_length=10)),
                ('rut_C', models.CharField(default='', max_length=15)),
                ('direccion_c', models.CharField(default='', max_length=50)),
                ('email_C', models.CharField(default='', max_length=30)),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
        migrations.AddField(
            model_name='abogado',
            name='direccion',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='abogado',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='abogado',
            name='rut',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(default='', max_length=500)),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('prediccion', models.CharField(default='', max_length=20)),
                ('plantilla', models.TextField(default='', max_length=500)),
                ('abogado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.abogado')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
            ],
            options={
                'db_table': 'Solicitud',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_documento', models.DateField()),
                ('solicitud', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.solicitud')),
            ],
            options={
                'db_table': 'Documento',
            },
        ),
    ]
