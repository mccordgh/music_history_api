from django.contrib import admin
from music_history_api import models

admin.site.register(models.Artist)
admin.site.register(models.Album)
admin.site.register(models.Song)
admin.site.register(models.Genre)