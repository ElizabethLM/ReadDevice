# Generated by Django 5.0.3 on 2024-03-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('puertos', models.CharField(max_length=200)),
            ],
        ),
    ]
