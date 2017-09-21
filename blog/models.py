from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    category = models.ForeignKey("Category")
    content = models.TextField()

    class Meta:
        ordering = ['-date',]


class Category(models.Model):
    title = models.CharField(max_length=200)
    

