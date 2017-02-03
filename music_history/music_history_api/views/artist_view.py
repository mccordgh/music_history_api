from rest_framework import viewsets
from music_history_api.serializers import artist_serializer
from music_history_api.models import artist_model

class ArtistView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Artist model '''
    queryset = artist_model.Artist.objects.all().order_by('-title')
    serializer_class = artist_serializer.ArtistSerializer