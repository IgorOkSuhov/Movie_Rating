# Generated by Django 4.0.5 on 2022-08-16 07:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_alter_movie_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Igor Suhov', max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
