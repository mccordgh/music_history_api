from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Artist model. Expsoses the (title, date_formed) fields. '''
    class Meta:
        model = Artist
        fields = ('title', 'date_formed')
        
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Album model. Expsoses the (title, release_date, producer) fields. '''
    class Meta:
        model = Album
        fields = ('title', 'release_date', 'length', 'label')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Song model. Expsoses the (title, length, album, genre) fields. '''
    class Meta:
        model = Song
        fields = ('title', 'length', 'release_date', 'album', 'genre')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for Genre model. Expsoses the (title) field. '''
    class Meta:
        model = Genre
        fields = ('title',)

