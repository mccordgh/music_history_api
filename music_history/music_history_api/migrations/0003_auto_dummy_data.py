# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 18:56
from __future__ import unicode_literals
import os
from sys import path
from django.core.management import call_command
from django.core import serializers
from django.db import migrations


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'artists.json', app_label='music_history_api') 
    call_command('loaddata', 'genres.json', app_label='music_history_api') 
    call_command('loaddata', 'albums.json', app_label='music_history_api') 
    call_command('loaddata', 'songs.json', app_label='music_history_api') 

def unload_fixture(apps, schema_editor):
    "deleting entries for this model..."

    Artist = apps.get_model("music_history_api", "Artist")
    Artist.objects.all().delete()
    Album = apps.get_model("music_history_api", "Album")
    Album.objects.all().delete()
    Song = apps.get_model("music_history_api", "Song")
    Song.objects.all().delete()
    Genre = apps.get_model("music_history_api", "Genre")
    Genre.objects.all().delete()

class Migration(migrations.Migration):  

    dependencies = [
        ('music_history_api', '0002_auto_20170201_1438'),
    ]

    operations = [
        # migrations.RunPython(load_fixture),
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]