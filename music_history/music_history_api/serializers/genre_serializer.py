from rest_framework import serializers
from music_history_api import models

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Genre model. Expsoses the (title) field. '''
    class Meta:
        model = models.Genre
        fields = ('title',)