from rest_framework import serializers
from music_history_api.models import genre_model

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Genre model. Expsoses the (title) field. '''
    class Meta:
        model = genre_model.Genre
        fields = ('title',)