from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import SavedImage, Banner

class IndexView(generic.ListView):
    template_name='banners/index.html'
    context_object_name="latest_banner_list"

    def get_queryset(self):
        return Banner.objects.order_by('-id')

