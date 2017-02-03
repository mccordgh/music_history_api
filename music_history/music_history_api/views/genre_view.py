from rest_framework import viewsets
from music_history_api.serializers import genre_serializer
from music_history_api.models import genre_model

class GenreView(viewsets.ModelViewSet):
    ''' API Endpoint that displays Genre model '''
    queryset = genre_model.Genre.objects.all().order_by('-title')
    serializer_class = genre_serializer.GenreSerializer