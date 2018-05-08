from django.contrib import admin
from .models import Genre, Feature, Artist, Album, Song

# Register your models here.
admin.site.register(Genre)
admin.site.register(Feature)

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)

