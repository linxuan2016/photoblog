from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    category = models.ForeignKey("Category")
    post_image = models.ImageField(upload_to='post_image')
    image_name = models.CharField(max_length=200)
    content = HTMLField()

    class Meta:
        ordering = ['-date',]


class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

