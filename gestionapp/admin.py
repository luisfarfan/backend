from django.contrib import admin

# Register your models here.
from gestionapp.models import Articulo, Deposito, Cliente, Unidad, Programagasto

admin.site.register(Articulo)
admin.site.register(Deposito)
admin.site.register(Cliente)
admin.site.register(Programagasto)
admin.site.register(Unidad)

