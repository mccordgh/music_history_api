from rest_framework import viewsets
from music_history_api import serializers
from music_history_api import models

class ArtistView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Artist model '''
    queryset = models.Artist.objects.all().order_by('-title')
    serializer_class = serializers.ArtistSerializer

class AlbumView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Album model '''
    queryset = models.Album.objects.all().order_by('-title')
    serializer_class = serializers.AlbumSerializer

class SongView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Song model '''
    queryset = models.Song.objects.all().order_by('-title')
    serializer_class = serializers.SongSerializer

class GenreView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Genre model '''
    queryset = models.Genre.objects.all().order_by('-title')
    serializer_class = serializers.GenreSerializer

