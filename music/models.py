from django.db import models

# Create your models here.
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class Genre(TaggedItemBase)
    content_object = models.ForeignKey('Music') 

class Music(models.Model):
    title = models.CharField('Title', max_length=200)
    artist = models.CharField('Artist', max_length=100)
    release_date = models.DateField('Release Date')

    tags = TaggableManager()
    genres = TaggableManager(through=Genre)

    class Meta:
        ordering = ['name']
        abstract = True

    def __str__(self):
        return f"{self.name - self.artist}"

class Album(Music):
    best = models.BooleanField('Best')
    listen_date = models.DateField('Listen Date', auto_now_add=True)

class Song(Music):
    fantastic_find = models.BooleanField('Fantastic Find')
    listen_date = models.DateField('Listen Date', auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
