from rest_framework import serializers
from music_history_api.models import artist_model

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Artist model. Expsoses the (title, date_formed) fields. '''
    class Meta:
        model = artist_model.Artist
        fields = ('title', 'date_formed')