from django.db import models

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
