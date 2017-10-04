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
    model = Image_Link_New
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



class Footer_Plugin(CMSPluginBase):
    model = Footer_New
    name = "Footer"
    render_template = "footer.html"

    def render(self, context, instance, placeholder):
        context.update({
            'logo': instance.logo,
            'logo_facebook': instance.logo_facebook,
            'logo_twitter': instance.logo_twitter,
            'logo_weibo': instance.logo_weibo,
            'link_url_1': instance.link_url_1,
            'link_url_2': instance.link_url_2,
            'link_url_3': instance.link_url_3,
            'link_url_4': instance.link_url_4,
            'link_url_5': instance.link_url_5,
            'link_url_6': instance.link_url_6,
            'link_url_7': instance.link_url_7,
            'link_url_8': instance.link_url_8,
            'link_url_9': instance.link_url_9,
            'cpright_field': instance.cpright_field,
            'text_1': instance.text_1,
            'text_2': instance.text_2,
            'text_3': instance.text_3,
            'text_4': instance.text_4,
            'text_5': instance.text_5,
            'text_6': instance.text_6,
            'text_7': instance.text_7,
            'text_8': instance.text_8,
            'text_9': instance.text_9,
            'text_facebook': instance.text_facebook,
            'text_twitter': instance.text_twitter,
            'text_weibo': instance.text_weibo,
        })
        return context



plugin_pool.register_plugin(My_Pictures_Plugin)
plugin_pool.register_plugin(Image_Link_Plugin)
plugin_pool.register_plugin(Footer_Plugin)
