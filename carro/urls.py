from django.urls import path
from .views import agregar_producto, eliminar_producto, restar_producto, limpiar_carro

app_name = 'carro'

urlpatterns = [
    path('agregar/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('restar/<int:producto_id>/', restar_producto, name='restar_producto'),
    path('limpiar/', limpiar_carro, name='limpiar_carro'),
]
