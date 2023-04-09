# Generated by Django 4.1.7 on 2023-04-09 09:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autopark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20)])),
                ('model', models.CharField(max_length=20)),
                ('year', models.DateField()),
                ('autopark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='autopark.autoparkmodel')),
            ],
            options={
                'verbose_name': 'car',
                'db_table': 'cars',
            },
        ),
    ]
