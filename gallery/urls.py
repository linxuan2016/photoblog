from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^photo-landscape/$', views.photo_landscape, name='landscape_detail'),
    url(r'^photo-street/$',views.photo_street, name='street_detail'),
    url(r'^photo-portrait/$',views.photo_portrait, name='portrait_detail'),
    url(r'^photo-landscape/(?P<l_id>[\-\w]+)/$',views.landscape_slideshow),
    url(r'^photo-street/(?P<s_id>[\-\w]+)/$',views.street_slideshow),
    url(r'^photo-portrait/(?P<p_id>[\-\w]+)/$',views.portrait_slideshow),


]
