from django.db import models
from music_history_api.models import album_model, genre_model

class Song(models.Model):
    '''The Song table maintains relevant information for each artist'''
    title = models.CharField(max_length=128)
    song_length = models.IntegerField()
    release_date = models.DateTimeField()
    album = models.ForeignKey(album_model.Album)
    genre = models.ForeignKey(genre_model.Genre)

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return '{}'.format(self.title)
