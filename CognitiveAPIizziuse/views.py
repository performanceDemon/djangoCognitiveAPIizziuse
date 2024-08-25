from django.contrib.auth import login, authenticate, get_user_model  # Importa authenticate para autenticar usuarios
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse
from .forms.login_form import LoginForm
from .forms.RegistroForm import RegistroForm
from .forms.CognitiveHomeForm import CognitiveHomeForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Obtén el modelo de usuario personalizado
Usuario = get_user_model()

def home(request):
    return HttpResponse("Bienvenido a mi proyecto!")

class MiVista(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response({"mensaje": "Hola, mundo!"})

class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return Response({'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)  # Actualiza esto si estás usando AuthenticationForm
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Intentando autenticar con username: {username} y password: {password}")  # Depuración
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Usuario autenticado correctamente")
                return redirect('cognitive_home')  # Redirige a la URL de cognitive_home
            else:
                print("Usuario o contraseña incorrectos")  # Depuración
                form.add_error(None, 'Usuario o contraseña incorrectos')
        else:
            print("Formulario inválido")  # Depuración
        return Response({'form': form})


class RegistroView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registro.html'

    def get(self, request):
        form = RegistroForm()
        return Response({'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  # Crea y guarda el nuevo usuario
            # Inicia sesión al usuario después de registrarse (opcional)
            # login(request, user)  # Descomenta si quieres iniciar sesión al usuario automáticamente
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión

        # Si el formulario no es válido, vuelve a mostrar el formulario con errores
        return Response({'form': form})

#class CognitiveHomeView(LoginRequiredMixin, APIView):
class CognitiveHomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cognitive_home.html'

    def get(self, request):
        form = CognitiveHomeForm()  # Instancia el formulario
        return Response({'form': form}, template_name='cognitive_home.html')

    def post(self, request):
        form = CognitiveHomeForm(request.POST)  # Instancia el formulario con los datos del POST
        if form.is_valid():
            # Simulamos la respuesta del API
            response_data = {'message': 'El análisis de sentimientos dice que estás contento'}
            return Response({'form': form, 'response_data': response_data}, template_name='cognitive_home.html')
        return Response({'form': form}, template_name='cognitive_home.html')