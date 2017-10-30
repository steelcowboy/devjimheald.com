from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('Post Title', max_length=200)
    author = models.CharField('Author', max_length=50)
    date_published = models.DateTimeField('Published', auto_now_add=True)
    most_recent = models.DateTimeField('Edited', auto_now=True)
