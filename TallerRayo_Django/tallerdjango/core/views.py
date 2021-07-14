from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'core/home.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def agendar(request):
    return render(request, 'core/agendar.html')

def cajasdecambio(request):
    return render(request, 'core/cajasdecambio.html')

def clima(request):
    return render(request, 'core/clima.html')

def direccion(request):
    return render(request, 'core/direccion.html')

def electronicaauto(request):
    return render(request, 'core/electronicaauto')

def geolocalizacion(request):
    return render(request, 'core/geolocalizacion')    

def inicioperfil(request):
    return render(request, 'core/inicioperfil')

def mantencion(request):
    return render(request, 'core/mentencion')

def perfiltrabajador(request):
    return render(request, 'core/perfiltrabajador')

def quienessomos(request):
    return render(request, 'core/quienessomos')

def servicios(request):
    return render(request, 'core/servicios')

def suspension(request):
    return render(request, 'core/suspension')

def vehiculo(request):
    return render(request, 'core/vehiculo')
