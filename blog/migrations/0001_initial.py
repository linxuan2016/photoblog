# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('post_image', models.ImageField(upload_to='post_image')),
                ('image_name', models.CharField(max_length=200)),
                ('content', djangocms_text_ckeditor.fields.HTMLField()),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
