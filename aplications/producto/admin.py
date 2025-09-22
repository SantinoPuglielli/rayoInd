from django.contrib import admin
from .models import Producto
from atexit import register
# Register your models here.
admin.site.register(Producto)