from django.db import models

class Genre(models.Model):
    '''The Genre table maintains relevant information for each artist'''
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        return '{}'.format(self.title)
