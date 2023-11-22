from django.contrib import admin
from . models import Usuario
from . models import Ofertas
from . models import Image

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Ofertas)
admin.site.register(Image)
