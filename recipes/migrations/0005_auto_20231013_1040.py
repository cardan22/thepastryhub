# Generated by Django 3.2.21 on 2023-10-13 10:40

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=djrichtextfield.models.RichTextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=djrichtextfield.models.RichTextField(max_length=10000),
        ),
    ]
