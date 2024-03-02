from genres.models import Genre
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.permissions import GenrePermissionClass
from genres.serializers import GenreModelSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass, GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer

