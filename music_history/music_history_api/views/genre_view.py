from rest_framework import viewsets
from music_history_api import serializers
from music_history_api import models

class GenreView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Genre model '''
    queryset = models.Genre.objects.all().order_by('-title')
    serializer_class = serializers.GenreSerializer