from django.db import models

class Artist(models.Model):
    '''The Artist table maintains relevant information for each artist'''
    title = models.CharField(max_length=128)
    date_formed = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return '{}'.format(self.title)

class Album(models.Model):
    '''The Album table maintains relevant information for each artist'''
    title = models.CharField(max_length=128)
    release_date = models.DateTimeField()
    album_length = models.IntegerField()
    record_label = models.CharField(max_length=128)
    artist = models.ManyToManyField(Artist)

    class Meta:
        verbose_name_plural = 'Albums'

    def __str__(self):
        return '{}'.format(self.title)

class Genre(models.Model):
    '''The Genre table maintains relevant information for each artist'''
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        return '{}'.format(self.title)

class Song(models.Model):
    '''The Song table maintains relevant information for each artist'''
    title = models.CharField(max_length=128)
    song_length = models.IntegerField()
    release_date = models.DateTimeField()
    album = models.ForeignKey(Album)
    genre = models.ForeignKey(Genre)

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return '{}'.format(self.title)

