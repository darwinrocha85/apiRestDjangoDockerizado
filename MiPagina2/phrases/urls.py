# Django
from django.urls import include, path
# Django Rest Framework
from rest_framework import routers
# Views
from . import views
router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename='authors')
router.register(r'phrases', views.PhraseViewSet, basename='phrases')
urlpatterns = [
    path('', include(router.urls)),
]
