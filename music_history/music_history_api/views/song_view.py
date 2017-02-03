from rest_framework import viewsets
from music_history_api import serializers
from music_history_api import models

class SongView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Song model '''
    queryset = models.Song.objects.all().order_by('-title')
    serializer_class = serializers.SongSerializer
