# Generated by Django 3.2.9 on 2021-12-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=64)),
                ('student', models.CharField(max_length=64)),
                ('exam', models.CharField(max_length=64)),
            ],
        ),
    ]
