# Generated by Django 4.0.5 on 2022-08-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('E', 'Euro'), ('D', 'Dollar'), ('G', 'Grivna')], default='G', max_length=1),
        ),
    ]
