from rest_framework import serializers
from music_history_api import models

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Album model. Expsoses the (title, release_date, producer) fields. '''
    class Meta:
        model = models.Album
        fields = ('title', 'release_date', 'album_length', 'record_label', 'artist')