# Generated by Django 4.2.1 on 2023-06-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc1', models.CharField(max_length=255)),
                ('desc2', models.CharField(max_length=255)),
                ('bday', models.DateTimeField()),
                ('web', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('deg', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('dispo', models.CharField(max_length=255)),
                ('desc3', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('icon', models.CharField(choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2'), ('choice3', 'Choice 3'), ('choice4', 'Choice 4'), ('choice5', 'Choice 5'), ('choice6', 'Choice 6')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
    ]
