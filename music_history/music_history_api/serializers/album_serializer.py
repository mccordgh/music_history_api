from rest_framework import serializers
from music_history_api.models import album_model

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Album model. Expsoses the (title, release_date, producer) fields. '''
    class Meta:
        model = album_model.Album
        fields = ('title', 'release_date', 'album_length', 'record_label', 'artist')