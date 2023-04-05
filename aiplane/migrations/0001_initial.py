# Generated by Django 4.1.7 on 2023-04-05 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirPlaneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{3,20}$', 'name must be 3-20 characters')])),
                ('speed', models.IntegerField(validators=[django.core.validators.MinValueValidator(100)])),
                ('engine', models.IntegerField()),
            ],
            options={
                'db_table': 'airplane',
            },
        ),
    ]
