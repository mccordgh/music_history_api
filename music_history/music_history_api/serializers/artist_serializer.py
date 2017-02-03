from rest_framework import serializers
from music_history_api import models

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Artist model. Expsoses the (title, date_formed) fields. '''
    class Meta:
        model = models.Artist
        fields = ('title', 'date_formed')