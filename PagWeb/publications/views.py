from django.shortcuts import render
from django.http import HttpResponse

from publications.models import Publications

def list_publications(request):
    publications = Publications.objects.all()
    context = {
        'publications' : publications,
    }
    return render(request, 'publications/list_publications.html', context=context)

