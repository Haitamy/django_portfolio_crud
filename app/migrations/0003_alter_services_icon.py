# Generated by Django 4.2.1 on 2023-06-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_about_bday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.CharField(choices=[('bi-briefcase', 'bi-briefcase'), ('bi-card-checklist', 'bi-card-checklist'), ('bi-bar-chart', 'bi-bar-chart'), ('bi-binoculars', 'bi-binoculars'), ('bi-brightness-high', 'bi-brightness-high'), ('bi-calendar4-week', 'bi-calendar4-week')], max_length=250),
        ),
    ]
