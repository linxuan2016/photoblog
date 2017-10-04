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



class Image_Link_New(CMSPlugin):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="image_link")
    text = models.CharField(max_length=200)
    link_url = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Image Link"

    def __unicode__(self):
        return "%s" % (self.name,)     


class Footer_New(CMSPlugin):
    logo = models.ImageField(upload_to="footer_logo")
    link_url_1 = models.CharField(max_length=200)
    text_1 = models.CharField(max_length=200)
    link_url_2 = models.CharField(max_length=200)
    text_2 = models.CharField(max_length=200)
    link_url_3 = models.CharField(max_length=200)
    text_3 = models.CharField(max_length=200)
    link_url_4 = models.CharField(max_length=200)
    text_4 = models.CharField(max_length=200)
    link_url_5 = models.CharField(max_length=200)
    text_5 = models.CharField(max_length=200)
    link_url_6 = models.CharField(max_length=200)
    text_6 = models.CharField(max_length=200)
    link_url_7 = models.CharField(max_length=200)
    text_7 = models.CharField(max_length=200)
    link_url_8 = models.CharField(max_length=200)
    text_8 = models.CharField(max_length=200)
    link_url_9 = models.CharField(max_length=200)
    text_9 = models.CharField(max_length=200)
    logo_facebook = models.ImageField(upload_to="footer_logo")
    text_facebook = models.CharField(max_length=200)
    logo_twitter = models.ImageField(upload_to="footer_logo")
    text_twitter = models.CharField(max_length=200)
    logo_weibo = models.ImageField(upload_to="footer_logo")
    text_weibo = models.CharField(max_length=200)
    cpright_field = models.TextField()


    class Meta:
        verbose_name = "Footer"

    def __unicode__(self):
        return "%s" % (self.name,)     


