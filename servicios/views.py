from django.shortcuts import render
from servicios.models import Producto
# Create your views here.

def servicios(request):
     
    servicios=Producto.objects.all()
    
    return render(request, "servicios/servicios.html", {"servicios": servicios})