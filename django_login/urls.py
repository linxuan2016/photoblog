from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import admin
from . import views




urlpatterns = [

    url(r'^login$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^register/$', views.register),

]
