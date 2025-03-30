# Generated by Django 5.1.7 on 2025-03-29 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_banner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='customerresponse',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='recipes.subcategory'),
        ),
    ]
