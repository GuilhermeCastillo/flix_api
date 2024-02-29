from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(
        validators = [
            MinValueValidator(0, "Avaliacao nao pode ser inferior a 0 estrelas."),
            MaxLengthValidator(5, "Avaliacao nao pode ser superior a 5 estrelas."),
        ]
    )
    comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.movie