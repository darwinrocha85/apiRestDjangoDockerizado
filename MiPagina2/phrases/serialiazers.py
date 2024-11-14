# Django Rest Framework
from rest_framework import serializers
# Models
from .models import Author, Phrase

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('slug', 'name', 'description')

class PhraseSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(source='author_slug', read_only=True,)

class Meta:
    model = Phrase
    fields = ('id', 'text', 'author_slug', 'author')
