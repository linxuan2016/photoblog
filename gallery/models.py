from django.db import models

class PhotoLandscape(models.Model):
    photo_landscape = models.ImageField(upload_to='photo_landscape')
    name = models.CharField(max_length=200)
    
    def next(self):
        try:
            return PhotoLandscape.objects.get(pk=self.pk+1)
        except:
            return None
    
    def previous(self):
        try:
            return PhotoLandscape.objects.get(pk=self.pk-1)
        except:
            return None

class PhotoStreet(models.Model):
    photo_street = models.ImageField(upload_to='photo_street')
    name = models.CharField(max_length=200)

    def next(self):
        try:
            return PhotoStreet.objects.get(pk=self.pk+1)
        except:
            return None
    
    def previous(self):
        try:
            return PhotoStreet.objects.get(pk=self.pk-1)
        except:
            return None

class PhotoPortrait(models.Model):
    photo_portrait = models.ImageField(upload_to='photo_portrait')
    name = models.CharField(max_length=200)

    def next(self):
        try:
            return PhotoPortrait.objects.get(pk=self.pk+1)
        except:
            return None
    
    def previous(self):
        try:
            return PhotoPortrait.objects.get(pk=self.pk-1)
        except:
            return None


