# Generated by Django 4.0.2 on 2022-03-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.CharField(max_length=30)),
                ('temperature', models.CharField(max_length=5)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
        ),
    ]
