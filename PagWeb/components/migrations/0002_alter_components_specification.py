# Generated by Django 4.1.5 on 2023-01-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='components',
            name='specification',
            field=models.CharField(default='', max_length=500),
        ),
    ]