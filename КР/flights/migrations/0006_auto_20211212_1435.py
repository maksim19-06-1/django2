# Generated by Django 3.2.9 on 2021-12-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='city',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
