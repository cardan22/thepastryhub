# Generated by Django 3.2.21 on 2023-11-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20231016_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]