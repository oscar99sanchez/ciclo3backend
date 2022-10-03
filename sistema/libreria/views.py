from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mouses
from .forms import MouseForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nostros.html')

def libros(request):
    libros = Mouses.objects.all()
    return render(request, 'libros/index.html', {'libros': libros}) 

@login_required
def crear(request):
    formulario = MouseForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})
@login_required
def editar(request, id):
    libros = Mouses.objects.all()
    return render(request, 'libros/index.html')
@login_required
def eliminar(request, id):
    libro = Mouses.objects.get(id=id)
    libro.delete()
    return redirect('libros')

# vistas de login

def singup(request):
    if request.method == 'GET':
        return render(request, 'paginas/singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'paginas/singup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'paginas/singup.html', {
            'form': UserCreationForm,
            'error': 'contraseña no coincide'
        })

@login_required
def singout(request):
    logout(request)
    return redirect('inicio')

def singin(request):
    if request.method == 'GET':
        return render(request, 'paginas/singin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            print(user.password)
            return render(request, 'paginas/singin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('inicio')

    
