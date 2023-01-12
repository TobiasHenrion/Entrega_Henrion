from django.shortcuts import render
from django.http import HttpResponse

from publications.models import Publications
from publications.forms import PublicationsForm

def list_publications(request):
    if 'search' in request.GET:
        search = request.GET['search']
        publications = Publications.objects.filter(category__contains = search)
    else: 
        publications = Publications.objects.all()

    context = {
        'publications' : publications,
    }
    return render(request, 'publications/list_publications.html', context=context)


def create_publications(request):
    if request.method == 'GET':
        context = {
            'form' : PublicationsForm(),
        }
    elif request.method == 'POST':
        
        form = PublicationsForm(request.POST, request.FILES)
        if form.is_valid():
            Publications.objects.create(
                name = form.cleaned_data['name'],
                category = form.cleaned_data['category'],
                marca = form.cleaned_data['marca'],
                meth = form.cleaned_data['meth'],
                notes = form.cleaned_data['notes'],
                img = form.cleaned_data['img'],
                price = form.cleaned_data['price'],
                change = form.cleaned_data['change']
                )
            
            context = {
                'message' : 'Se ha publicado correctamente'
            }
                
            
        else:
            context = {
                'message' : "ojo al piojo con los siguientes errores",
                'form_errors' : form.errors,
                'form' : PublicationsForm,
            }        


        



        
    return render(request, 'publications/create_publications.html', context=context)
