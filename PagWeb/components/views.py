from django.shortcuts import render
from django.http import HttpResponse

from components.models import Components
from components.forms import ComponentsForm


def list_components(request):

    components = Components.objects.all()
    context = {
        'components' : components
    }

    return render(request, 'components/list_components.html', context=context)

def create_components(request):
    if request.method == 'GET':
        context = {
            'form' : ComponentsForm()
        }
    elif request.method == 'POST':
        form = ComponentsForm(request.POST)
        if form.is_valid():
            Components.objects.create(
                name = form.cleaned_data['name'],
                category = form.cleaned_data['category'],
                marca = form.cleaned_data['marca'],
                specification = form.cleaned_data['specification'],
                price = form.cleaned_data['price'],
        )
            context={
                'message' : 'Componente creado existosamente'
            }
        else:
            context ={
                'form_errors' : form.errors,
                'form' : ComponentsForm()
            }
        
    return render(request, 'components/create_components.html', context=context)