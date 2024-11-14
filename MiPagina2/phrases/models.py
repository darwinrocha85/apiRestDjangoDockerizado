from django.db import models

# Create your models here.
from django.db import models
class Author(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
class Meta:
    db_table = 'authors'
class Phrase(models.Model):
    author_slug = models.ForeignKey(Author, db_column='author_slug', on_delete=models.DO_NOTHING)
    text = models.TextField()
class Meta:
    db_table = 'phrases'
