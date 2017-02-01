from rest_framework import serializers
from music_history_api import models

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Artist model. Expsoses the (title, date_formed) fields. '''
    class Meta:
        model = models.Artist
        fields = ('title', 'date_formed')
        
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Album model. Expsoses the (title, release_date, producer) fields. '''
    class Meta:
        model = models.Album
        fields = ('title', 'release_date', 'album_length', 'record_label', 'artist')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Song model. Expsoses the (title, length, album, genre) fields. '''
    class Meta:
        model = models.Song
        fields = ('title', 'song_length', 'release_date', 'album', 'genre')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Genre model. Expsoses the (title) field. '''
    class Meta:
        model = models.Genre
        fields = ('title',)

