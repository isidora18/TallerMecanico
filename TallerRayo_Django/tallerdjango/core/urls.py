from django.urls import path
from .views import home,agendar,cajasdecambio,clima,direccion,electronicaauto,formulario,geolocalizacion,inicioperfil,mantencion,perfiltrabajador,quienessomos,servicios,suspension,vehiculo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('Home',home,name="home")  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    path('agendar',agendar,name="agendar"),
    path('cajasdecambio',cajasdecambio, name="cajasdecambio"),
    path('clima',clima, name="Clima"),
    path('direccion', direccion, name="Direccion"),
    path('Electronicaauto', electronicaauto, name="Electronica Auto"),
    path('formulario',formulario, name="Formulario"),
    path('geolocalizacion',geolocalizacion, name="Geo Localizacion"),
    path('inicioperfil',inicioperfil, name="registro"),
    path('mantencion',mantencion,name="Mantencion"),
    path('perfiltrabajador',perfiltrabajador, name="Perfil del Trabajador"),
    path('quienessomos',quienessomos, name="Quienes Somos"),
    path('servicios',servicios, name="Servicios"),
    path('vehichulos',vehiculo, name="Vehiculos")
    
]