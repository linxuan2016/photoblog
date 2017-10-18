from django.db import models

class PhotoLandscape(models.Model):
    photo_landscape = models.ImageField(upload_to='photo_landscape')
    name = models.CharField(max_length=200)

class PhotoStreet(models.Model):
    photo_street = models.ImageField(upload_to='photo_street')
    name = models.CharField(max_length=200)

class PhotoPortrait(models.Model):
    photo_portrait = models.ImageField(upload_to='photo_portrait')
    name = models.CharField(max_length=200)
