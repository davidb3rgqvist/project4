# Generated by Django 5.0.6 on 2024-05-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_recipe_created_at_recipe_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
