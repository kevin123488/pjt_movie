from django.db import models
from django.conf import settings


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


        


class Movie(models.Model):
    movienumber = models.IntegerField(null=True)
    title = models.CharField(max_length=10000, null=True)
    release_date = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=50000, null=True)
    adult = models.BooleanField(null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    

    