# Generated by Django 4.1.5 on 2023-01-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='change',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='publications',
            name='img',
            field=models.ImageField(default='', upload_to='publications'),
        ),
        migrations.AddField(
            model_name='publications',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
