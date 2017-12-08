from django.db import models
from datetime import date
from django.core.urlresolvers import reverse

ITEM_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('P', 'Portion'),
)


def default_city():
    return "Made in Mumbai"


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=150)
    album_log = models.FileField()
    repeat_song = models.IntegerField()
    date = models.DateField(default=date.today)
    city = models.CharField(max_length=30, default=default_city)
    comment = models.TextField()


    def __unicode__(self):
        return self.artist 

    def get_absolute_url(self):
        return reverse('album_edit', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, db_index=False)
    is_active = models.BooleanField('Active?', default=True)
    file_type = models.CharField(max_length=1000)
    size = models.CharField(choices=ITEM_SIZES, max_length=1)
    song_title = models.CharField(max_length=250)

    def __unicode__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('song_edit', kwargs={'pk': self.pk})
