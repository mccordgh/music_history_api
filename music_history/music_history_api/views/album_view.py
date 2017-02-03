from rest_framework import viewsets
from music_history_api import serializers
from music_history_api import models

class AlbumView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Album model '''
    queryset = models.Album.objects.all().order_by('-title')
    serializer_class = serializers.AlbumSerializer