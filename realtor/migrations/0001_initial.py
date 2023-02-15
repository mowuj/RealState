# Generated by Django 4.1.7 on 2023-02-15 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('biodata', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='realtor')),
                ('top_seller', models.BooleanField(default=False)),
                ('date_hired', models.DateField(default=datetime.datetime(2023, 2, 15, 18, 15, 38, 811818))),
            ],
        ),
    ]
