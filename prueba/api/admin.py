from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Abogado)
admin.site.register(Cliente)
admin.site.register(Solicitud)
admin.site.register(Documento)

