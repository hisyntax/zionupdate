from django.db import models
from django.urls import reverse
class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SermonMinister(models.Model):
    minister = models.CharField(max_length=100, default='minister')

    def __str__(self):
        return self.minister

class SermonYear(models.Model):
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.year

class SongMinister(models.Model):
    minister = models.CharField(max_length=100, default='minister')

    def __str__(self):
        return self.minister

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class Sermon(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    timestamp = models.DateTimeField(auto_now_add=True)
    sermon = models.FileField(upload_to='sermons', blank=True, null=True)
    minister = models.ManyToManyField(SermonMinister)
    tag = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    year = models.ManyToManyField(SermonYear)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('playSermon', kwargs={
            'id': self.id
        })


class Song(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    timestamp = models.DateTimeField(auto_now_add=True)
    song = models.FileField(upload_to='songs', blank=True, null=True)
    minister = models.ManyToManyField(SongMinister)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('playSong', kwargs={
            'id': self.id
        })

class Article(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    timestamp = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('readArticle', kwargs={
            'id': self.id
        })
