from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^photo-landscape/$', views.photo_landscape, name='landscape_detail'),
    url(r'^photo-street/$',views.photo_street, name='street_detail'),
    url(r'^photo-portrait/$',views.photo_portrait, name='portrait_detail'),

]
