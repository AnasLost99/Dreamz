# Generated by Django 3.2.23 on 2024-01-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20240117_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.CharField(max_length=1130),
        ),
    ]
