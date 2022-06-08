from ast import IsNot
from distutils import errors
from msilib.schema import Error
from multiprocessing.reduction import send_handle
from tkinter.tix import Form
from xml.dom import INVALID_ACCESS_ERR
from django import http
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm


# Create your views here.

def formulario (request):
    return render(request, 'core/formulario.html')

def correas (request):
    return render(request, 'core/correas.html')

def Mascotas (request):
    return render(request, 'core/Mascotas.html')

def bandanas (request):
    return render(request, 'core/bandanas.html')

def identificaciones(request):
    return render(request, 'core/identificaciones.html')

def home(request):
    producto = Producto.objects.all()
    datos = {
        'producto': producto
    }
    return render(request, 'core/home.html', datos)

def correas(request):
    producto = Producto.objects.all()
    datos = {
        'producto': producto
    }
    return render(request, 'core/correas.html', datos)


def bandanas(request):
    producto = Producto.objects.all()
    datos = {
        'producto': producto
    }
    return render(request, 'core/bandanas.html', datos)

def identificaciones(request):
    producto = Producto.objects.all()
    datos = {
        'producto': producto
    }
    return render(request, 'core/identificaciones.html', datos)

def form_Producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            
        
    return render(request, 'core/form_Producto.html', datos)

def form_mod_Producto(request, id):
    producto = Producto.objects.get(Id=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_Producto.html', datos)

def form_del_Producto(request, id):
    producto = Producto.objects.get(Id=id)
    producto.delete() 
    return redirect(to="home")


