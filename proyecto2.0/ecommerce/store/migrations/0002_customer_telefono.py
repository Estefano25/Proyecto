# Generated by Django 4.1.2 on 2023-06-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Telefono',
            field=models.FloatField(null=True),
        ),
    ]
