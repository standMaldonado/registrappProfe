from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

# Create your views here.

def asignaturas(request):
    # Aquí va tu código para manejar la solicitud a '/asignaturas/'
    return render(request, 'asignaturas.html')

def inicio_docente(request):
    # Aquí va tu código para manejar la solicitud a '/inicio-docente/'
    return render(request, 'inicio-docente.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('nombreUsuario')  # usa get en lugar de []
        password = request.POST.get('contrasena')  # usa get en lugar de []
        if username and password:
            user = Usuario.objects.filter(NOM_USUARIO=username, CONTRASENA=password).first()
            if user:
                return redirect('inicio-docente')  # replace 'home' with the name of the view you want to redirect to after login
            else:
                return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def olvide_contrasena(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        try:
            usuario = Usuario.objects.get(NOM_USUARIO=nombreUsuario)
            return render(request, 'olvide-contrasena.html', {'message': f'La contraseña para {nombreUsuario} es {usuario.CONTRASENA}'})
        except Usuario.DoesNotExist:
            return render(request, 'olvide-contrasena.html', {'error': 'Usuario no encontrado'})
    return render(request, 'olvide-contrasena.html')

def registro(request):
    if request.method == 'POST':
        username = request.POST['nombreUsuario']
        password = request.POST['contrasena']
        Usuario.objects.create(NOM_USUARIO=username, CONTRASENA=password)
        return redirect('login')
    return render(request, 'registro.html')