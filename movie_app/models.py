from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Actor(models.Model):
    Male = 'M'
    Famale = 'F'

    GENDERS = [
        (Male, 'Мужчина'),
        (Famale, 'Женщина'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS,default=Male)

    def __str__(self):
        if self.gender == self.Male:
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'



class Movie(models.Model):

    EURO = 'EUR'
    USD = 'USD'
    GRN = 'GRN'

    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollar'),
        (GRN, 'Grivna'),
    ]


    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=GRN)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)




    def get_url(self):
        return reverse('movie-detail', args=[self.id])


    def __str__(self):
        return f'{self.name} - {self.rating}%'

#from movie_app.models import Movie
#  Movie(name='xxx',rating=75).save()
