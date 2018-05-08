from django.db import models
from django_countries.fields import CountryField

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


# Genre Tagging
class GenreThru(GenericTaggedItemBase):
    tag = models.ForeignKey('Genre', 
            related_name="%(app_label)s_%(class)s_items", 
            on_delete=models.CASCADE)

class Genre(TagBase):
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

class FeatureThru(GenericTaggedItemBase):
    tag = models.ForeignKey('Feature', 
            related_name="%(app_label)s_%(class)s_items", 
            on_delete=models.CASCADE)

class Feature(TagBase):
    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

# Library Components
class Artist(models.Model):
    name = models.CharField('Title', max_length=200)
    country = CountryField(blank=True, null=True)
    genres = TaggableManager('Genres', through=GenreThru)
    comments = models.TextField('Comments', max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Music(models.Model):
    title = models.CharField('Title', max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField('Release Date')
    listen_date = models.DateField('Listen Date', blank=True, null=True)
    notes = models.TextField('Notes', blank=True, null=True)

    genres = TaggableManager('Genres', through=GenreThru)

    class Meta:
        ordering = ['-release_date']
        abstract = True

    def __str__(self):
        return f"{self.title} - {self.artist}"

class Album(Music):
    best = models.BooleanField('Best')
    todo = models.BooleanField('TODO')

class Song(Music):
    fantastic_find = models.BooleanField('Fantastic Find')
    features = TaggableManager('Features', through=FeatureThru)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
