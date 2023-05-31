from django.db import models
from django.urls import reverse
from datetime import date

TOOLONG = (
    ('Y', 'Yes'),
    ('N', 'No'),
    ('NR', 'Not Really'),
)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    published = models.IntegerField()

    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    def chapter_for_today(self):
        return self.chapter_set.filter(date=date.today()).count() >= 3
    
class Chapter(models.Model):
    date = models.DateField('Date Read')
    numchapters = models.IntegerField('How many chapters read', default=1)

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'{self.numchapters} chapter(s) read on: {self.date}'
    class Meta:
        ordering = ['-date']