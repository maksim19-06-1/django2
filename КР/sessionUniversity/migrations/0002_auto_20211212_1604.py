# Generated by Django 3.2.9 on 2021-12-12 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessionUniversity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('birthDate', models.DateTimeField()),
                ('gender', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('semester', models.CharField(max_length=64)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='SessionUniversity',
        ),
        migrations.AddField(
            model_name='exam',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='sessionUniversity.student'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='sessionUniversity.subject'),
        ),
    ]
