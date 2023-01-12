from django.shortcuts import render
from django.http import HttpResponse

from users.models import Users
from users.forms import UserForm


def register(request):
    if request.method == 'GET':
        context ={
            'form': UserForm()
        }
    elif request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            Users.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                birth = form.cleaned_data['birth'],
            )    
            context = {
                'message' : 'Se ha registrado correctamente'
            }
        else:
            context = {
                'message' : "ojo al piojo con los siguientes errores",
                'form_errors' : form.errors,
                'form' : UserForm
            } 
    return render(request, 'users/register.html', context=context)

