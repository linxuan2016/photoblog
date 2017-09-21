from django.shortcuts import render
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *

class My_Pictures_Plugin(CMSPluginBase):
    text_enabled = True
    model = My_Pictures
    name = "My Pictures"
    render_template = "my_picture.html"

    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'description': instance.description,
            'price': instance.price

        })
        return context


class Image_Link_Plugin(CMSPluginBase):
    text_enabled = True
    model = Image_Link
    name = "Image Link"
    render_template = "image_link.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'text': instance.text,
            'link_url': instance.link_url
        })
        return context


plugin_pool.register_plugin(My_Pictures_Plugin)
plugin_pool.register_plugin(Image_Link_Plugin)
