from django.db import models
from djangocms_text_ckeditor.fields import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    category = models.ForeignKey("Category")
    post_image = models.ImageField(upload_to='post_image')
    image_name = models.CharField(max_length=200)
    content = HTMLField()

    class Meta:
        ordering = ['-date',]
    def next(self): 
        try:
            return Post.objects.get(pk=self.pk-1)
        except:
            return None
    
    def previous(self):
        try: 
            return Post.objects.get(pk=self.pk+1)
        except:
            return None



class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

