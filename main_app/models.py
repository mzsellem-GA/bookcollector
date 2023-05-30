from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    published = models.IntegerField()

    def __str__(self):
        return f'{self.title} ({self.id})'

