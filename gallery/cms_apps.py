from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class GalleryApp(CMSApp):
    name = "Gallery"
    app_name = "gallery"
    urls = ["gallery.urls"]

apphook_pool.register(GalleryApp)

