from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.blog),
    url(r'^category/(?P<c_id>[\-\w]+)/$', views.category, name='category_detail'),
    url(r'^post/(?P<p_id>[\-\w]+)/$',views.post, name='post_detail'),
   
]
