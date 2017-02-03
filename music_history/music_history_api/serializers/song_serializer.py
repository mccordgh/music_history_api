from rest_framework import serializers
from music_history_api.models import song_model

class SongSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Song model. Expsoses the (title, length, album, genre) fields. '''
    class Meta:
        model = song_model.Song
        fields = ('title', 'song_length', 'release_date', 'album', 'genre')