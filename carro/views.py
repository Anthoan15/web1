from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .carro import Carro
from tienda.models import Producto

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response_data = {
            'status': 'ok',
            'total_items': carro.cantidad_total(),
            'carro': carro.carro,
            'importe_total_carro': sum(float(item['precio']) for item in carro.carro.values()),
            'widget': render_to_string('carro/widget.html', {'carro': carro.carro})
        }
        return JsonResponse(response_data)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response_data = {
            'status': 'ok',
            'total_items': carro.cantidad_total(),
            'carro': carro.carro,
            'importe_total_carro': sum(float(item['precio']) for item in carro.carro.values()),
            'widget': render_to_string('carro/widget.html', {'carro': carro.carro})
        }
        return JsonResponse(response_data)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_compra(producto=producto)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response_data = {
            'status': 'ok',
            'total_items': carro.cantidad_total(),
            'carro': carro.carro,
            'importe_total_carro': sum(float(item['precio']) for item in carro.carro.values()),
            'widget': render_to_string('carro/widget.html', {'carro': carro.carro})
        }
        return JsonResponse(response_data)
    return redirect("tienda")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response_data = {
            'status': 'ok',
            'total_items': carro.cantidad_total(),
            'carro': carro.carro,
            'importe_total_carro': 0,
            'widget': render_to_string('carro/widget.html', {'carro': carro.carro})
        }
        return JsonResponse(response_data)
    return redirect("tienda")
