# Generated by Django 5.1.7 on 2025-03-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_customerresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', height_field=300, upload_to='media'),
        ),
    ]
