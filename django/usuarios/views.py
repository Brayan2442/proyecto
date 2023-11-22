
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Usuario
from .models import Ofertas
from .forms import OfertaForm
from .forms import ImageForm


# Create your views here.
# def usuariolist(request):
#     return render(request,"usuariolist.html")


def usuariolist(request):
    get_usuarios=Usuario.objects.all()
    data={
        'get_usuarios':get_usuarios
    }
    return render(request,'usuariolist.html',data)

def postulaciones(request):
    data=Ofertas.objects.all()
    return render(request,'postulaciones.html',{'ofertas':data})


def guardar_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            # Puedes realizar acciones adicionales antes de guardar si es necesario
            form.save()
            return redirect('formulario_ofertas')  # Reemplaza 'nombre_de_tu_vista' con el nombre correcto de tu vista
    else:
        form = OfertaForm()

    # Puedes pasar datos adicionales al contexto del formulario si es necesario
    context = {'form': form}
    return render(request, 'formulario_ofertas.html', context)

from django.shortcuts import render, redirect
from .forms import OfertaForm

def formulario_ofertas(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
       
            form.save()
            return redirect('formulario_ofertas')  # Reemplaza 'nombre_de_tu_vista' con el nombre correcto de tu vista
    else:
        form = OfertaForm()


    context = {'form': form}
    return render(request, 'formulario_ofertas.html', context)



def Image(request):
    if request.method == 'POST':
        form =ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ImageForm()
    return render(request, "templates/postulaciones", {"form": form})