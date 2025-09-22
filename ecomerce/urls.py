from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from aplications.producto import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'),  # Ruta vacía apunta a la vista `index`
    path('productos/', views.productos, name='productos'),  # Nueva vista `productos`
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'), 
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),  
    path('detalleproducto/', TemplateView.as_view(template_name='detalleproducto.html'), name='detalleproducto'), 
    path('pago/', TemplateView.as_view(template_name='pago.html'), name='pago'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)