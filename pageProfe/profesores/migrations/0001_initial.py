# Generated by Django 4.2.2 on 2023-12-14 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOM_USUARIO', models.CharField(max_length=100, unique=True)),
                ('CONTRASENA', models.CharField(max_length=100)),
            ],
        ),
    ]
