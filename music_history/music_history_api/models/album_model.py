from django.db import models

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
