from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genres = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies") # um filme pode ter varios atores ligados nele
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    