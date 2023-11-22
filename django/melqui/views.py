from django.http import HttpResponse
from django.shortcuts import render
# from django.urls import path

# def home(request):
#     return HttpResponse('<h1>HOLAAAAAAAAA')

def home(request):
    return render(request,'inicio1.html')


def login(request):
    return render(request,'index1.html')

def agenda(request):
    return render(request,'agenda.html')

def hoja_vida(request):
    return render(request,'hoja_vida.html')

def notificaciones(request):
    return render(request,'notificaciones.html')

def postulaciones(request):
    return render(request,'postulaciones.html')

def navegador(request):
    return render(request,'navegador.html')

def contacta(request):
    return render(request,'contacta.html')

def formulario_ofertas(request):
    return render(request,'formulario_ofertas.html')

def nosotros(request):
    return render(request,'nosotros.html')


def usuarios(request):
    return render(request,'usuariolist.html')

