from django.contrib import admin
from .models import categorias, post


# Register your models here.
class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


class postAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(categorias, categoriaAdmin)
admin.site.register(post, postAdmin)