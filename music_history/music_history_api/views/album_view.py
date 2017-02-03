from rest_framework import viewsets
from music_history_api.serializers import album_serializer
from music_history_api.models import album_model

class AlbumView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Album model '''
    queryset = album_model.Album.objects.all().order_by('-title')
    serializer_class = album_serializer.AlbumSerializer