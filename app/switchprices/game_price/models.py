from django.db import models
from django.shortcuts import reverse


class Game(models.Model):
    title = models.CharField('Name of the game', max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    about = models.TextField(blank=True, db_index=True)
    image = models.ImageField(upload_to='images/images_game')
    data_sale = models.DateTimeField(auto_now_add=True)
    countries = models.ManyToManyField('Country', blank=True, related_name='')

    def get_absolute_url(self):
        return reverse('game_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Country(models.Model):
    country = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image_flag = models.ImageField(upload_to='images/images_flag')

    def __str__(self):
        return '{}'.format(self.title)


