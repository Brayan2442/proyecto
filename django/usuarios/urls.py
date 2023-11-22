from django.urls import path
from . import views


urlpatterns = [
    path('lista/', views.usuariolist, name="usuario_list"),
    path('lista1/', views.postulaciones, name="postulaciones"),
    path('formulario_ofertas/', views.formulario_ofertas, name='formulario_ofertas'),
    path('guardar_oferta/', views.guardar_oferta, name='guardar_oferta'),
    path('formulario_ofertas/', views.formulario_ofertas, name='formulario_ofertas'),
    path("postualante/",views.Image , name="postualante"),
  
         
]