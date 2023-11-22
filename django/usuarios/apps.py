from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

class OfertasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ofertas'

class ImageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image'
