# Generated by Django 4.2.20 on 2025-04-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='photos/category/'),
        ),
    ]
