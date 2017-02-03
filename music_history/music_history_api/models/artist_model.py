from django.db import models

class Artist(models.Model):
    '''The Artist table maintains relevant information for each artist'''
    title = models.CharField(max_length=128)
    date_formed = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return '{}'.format(self.title)
