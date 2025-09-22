from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Producto
from django.views.generic import TemplateView


from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request, 'index.html')

def productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'productos.html', context)
