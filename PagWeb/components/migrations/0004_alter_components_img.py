# Generated by Django 4.1.5 on 2023-01-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0003_components_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='components',
            name='img',
            field=models.ImageField(upload_to='componentes'),
        ),
    ]
