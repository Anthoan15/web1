from django.contrib import admin
from .models import categorias, Producto


# Register your models here.
class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(categorias, categoriaAdmin)
admin.site.register(Producto, ProductoAdmin)