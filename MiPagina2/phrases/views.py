from django.shortcuts import render

# Create your views here.
# Django Rest Framework
from rest_framework import viewsets
# Models
from .models import Author, Phrase
# Serializers
from .serializers import AuthorSerializer, PhraseSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class PhraseViewSet(viewsets.ModelViewSet):
    serializer_class = PhraseSerializer
    queryset = Phrase.objects.all()
