# Generated by Django 5.0.6 on 2024-06-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desserts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert',
            name='calories',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dessert',
            name='freshness_date',
            field=models.TextField(),
        ),
    ]
