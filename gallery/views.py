from django.shortcuts import render, get_object_or_404
from .models import *


def photo_landscape(request):
    context = {}
    photos_col_1 = PhotoLandscape.objects.filter(pk__in=range(1,1000,4))
    photos_col_2 = PhotoLandscape.objects.filter(pk__in=range(2,1000,4))
    photos_col_3 = PhotoLandscape.objects.filter(pk__in=range(3,1000,4))
    photos_col_4 = PhotoLandscape.objects.filter(pk__in=range(4,1000,4))
    context['photos_col_1'] = photos_col_1   
    context['photos_col_2'] = photos_col_2   
    context['photos_col_3'] = photos_col_3   
    context['photos_col_4'] = photos_col_4   
    return render(request, "photo_landscape.html", context)


def photo_street(request):
    context = {}
    photos_col_1 = PhotoStreet.objects.filter(pk__in=range(1,1000,4))
    photos_col_2 = PhotoStreet.objects.filter(pk__in=range(2,1000,4))
    photos_col_3 = PhotoStreet.objects.filter(pk__in=range(3,1000,4))
    photos_col_4 = PhotoStreet.objects.filter(pk__in=range(4,1000,4))
    context['photos_col_1'] = photos_col_1   
    context['photos_col_2'] = photos_col_2   
    context['photos_col_3'] = photos_col_3   
    context['photos_col_4'] = photos_col_4   
    return render(request, "photo_street.html", context)

def photo_portrait(request):
    context = {}
    photos_col_1 = PhotoPortrait.objects.filter(pk__in=range(1,1000,4))
    photos_col_2 = PhotoPortrait.objects.filter(pk__in=range(2,1000,4))
    photos_col_3 = PhotoPortrait.objects.filter(pk__in=range(3,1000,4))
    photos_col_4 = PhotoPortrait.objects.filter(pk__in=range(4,1000,4))
    context['photos_col_1'] = photos_col_1   
    context['photos_col_2'] = photos_col_2   
    context['photos_col_3'] = photos_col_3   
    context['photos_col_4'] = photos_col_4   
    return render(request, "photo_portrait.html", context)


def landscape_slideshow(request, l_id):
    context={}
    photo = get_object_or_404(PhotoLandscape, pk=l_id)
    photo_next = photo.next()
    photo_previous = photo.previous
    context['photo'] = photo
    context['photo_next'] = photo_next
    context['photo_previous'] = photo_previous

    return render(request, "landscape_slideshow.html", context)

def street_slideshow(request, s_id):
    context={}
    photo = get_object_or_404(PhotoStreet, pk=s_id)
    photo_next = photo.next()
    photo_previous = photo.previous
    context['photo'] = photo
    context['photo_next'] = photo_next
    context['photo_previous'] = photo_previous

    return render(request, "street_slideshow.html", context)

def portrait_slideshow(request, p_id):
    context={}
    photo = get_object_or_404(PhotoPortrait, pk=p_id)
    photo_next = photo.next()
    photo_previous = photo.previous
    context['photo'] = photo
    context['photo_next'] = photo_next
    context['photo_previous'] = photo_previous

    return render(request, "portrait_slideshow.html", context)
