from django.db import models
from cms.models.pluginmodel import CMSPlugin


class My_Pictures(CMSPlugin):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="my_pictures")
    description = models.TextField()
    price = models.CharField(max_length=10)

    class Meta:
        verbose_name = "My Picture"
        verbose_name_plural = "My Pictures"

    def __unicode__(self):
        return "%s" % (self.name,)



class Image_Link(CMSPlugin):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="image_link")
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Image Link"

    def __unicode__(self):
        return "%s" % (self.name,)     
