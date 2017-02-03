from rest_framework import viewsets
from music_history_api import serializers
from music_history_api import models

class ArtistView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Artist model '''
    queryset = models.Artist.objects.all().order_by('-title')
    serializer_class = serializers.ArtistSerializer