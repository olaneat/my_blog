from django.urls import reverse
import datetime
from django.utils import timezone
from .constant import stat, pub_status
from django.db import models

class Writer(models.Model):
  first_name = models.CharField(max_length = 150)
  surname = models.CharField(max_length = 130)

  def __str__(self):
    return ('{0}, {1}').format(self.first_name, self.surname)


class News(models.Model):
  name = models.ForeignKey(Writer, on_delete = models.CASCADE)
  title = models.CharField(max_length = 250)
  slug = models.SlugField(max_length = 300, unique_for_date = 'publish' )
  created = models.DateTimeField(auto_now_add = True)
  publish = models.DateTimeField(default = timezone.now)
  updated = models.DateTimeField(auto_now = True)
  status = models.CharField(max_length = 17, choices = pub_status)
  post = models.TextField(max_length = 1000)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
      return reverse('news-detail', args=[self.publish.year,
                                            self.publish.strftime('%m'),
                                            self.publish.strftime('%d'),
                                            self.slug])

  class Meta:
    ordering = ['-created',]


class Artist(models.Model):
  first_name = models.CharField(max_length = 100)
  surname = models.CharField(max_length = 150)
  stage_name = models.CharField(max_length = 100)
  status =models.CharField(max_length = 10, choices = stat)
  D_O_B = models.DateField()
  record_Label =models.CharField(max_length = 100)
  so_of_album = models.CharField(max_length = 50)
  image = models.ImageField()


  def get_absolute_url(self):
    return reverse('artist-detail', args = [str(self.id)])

  def __str__(self):
    return ('{0}, {1}').format(self.first_name, self.surname)

class Music(models.Model):
  title = models.CharField(max_length = 150)
  artist_name = models.ForeignKey(Artist, on_delete = models.CASCADE )
  music = models.FileField()
  music_name =models.CharField(max_length = 30)
  release_date = models.DateField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('music-detail', args = [str(self.id)])
  class Meta:
    ordering = ['-release_date',]

class Videos(models.Model):
  artist =models.ForeignKey(Artist, on_delete =models.CASCADE, blank = True)
  title = models.CharField(max_length = 50)
  release_date = models.DateField()
  video = models.FileField()

  def __str__(self):
      return self.title

  def get_absolute_url(self):
    return reverse('video-detail', args = [str(self.id)])

  class Meta:
    ordering = ['-release_date']

class Comment(models.Model):
  news = models.ForeignKey(News, on_delete = models.CASCADE, related_name = 'comments')
  name = models.CharField(max_length = 100)
  active = models.BooleanField(default = True)
  email =models.EmailField()
  body = models.TextField()
  created = models.DateTimeField(auto_now = True)
  
  class Meta:
    ordering = ('created',)

  def __str__(self):
    return ' comments by {} on {}'.format(self.name, self.news)
