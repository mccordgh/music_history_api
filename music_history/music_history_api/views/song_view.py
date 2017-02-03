from rest_framework import viewsets
from music_history_api.serializers import song_serializer
from music_history_api.models import song_model

class SongView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Song model '''
    queryset = song_model.Song.objects.all().order_by('-title')
    serializer_class = song_serializer.SongSerializer
