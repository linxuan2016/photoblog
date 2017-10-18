from django.shortcuts import render
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
