from django.shortcuts import render
from django.shortcuts import render
from links.models import Link, Tag
# Create your views here.

def index(request, tag = ''):
    if tag:
        links = Tag.objects.filter(tag=tag).get().link_set.all()
    else:
        links = Link.objects.all()
    return links
