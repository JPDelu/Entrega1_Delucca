# Generated by Django 4.1.3 on 2022-11-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_accesorio', models.CharField(max_length=50)),
                ('tipo_accesorio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_juego', models.CharField(max_length=50)),
                ('genero_juego', models.CharField(max_length=50)),
                ('precio_juego', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='consola',
            name='marca_consola',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='consola',
            name='nombre_consola',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='consola',
            name='precio_consola',
            field=models.IntegerField(default=None),
        ),
    ]
