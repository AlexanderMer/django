from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} -  {}'.format(self.album_title, self.artist)


class Song(models.Model):
    # CASCADE - if the album containing this song is deleted, our song gets deleted too as result
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return 'song: {}'.format(self.song_title)

class Producer(models.Model):
    producer_name = models.CharField(max_length=50)
