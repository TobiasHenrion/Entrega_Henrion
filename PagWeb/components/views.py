from django.shortcuts import render
from django.http import HttpResponse

from components.models import Components

def list_components(request):
    components = Components.objects.all()
    context = {
        components : 'components'
    }
    return render(request, 'components/list_components.html', context=context)