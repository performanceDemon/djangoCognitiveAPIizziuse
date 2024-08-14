from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from CognitiveAPIizziuse.forms.login_form import LoginForm
from django.shortcuts import redirect
from .forms.RegistroForm import RegistroForm
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse

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
        form = LoginForm(request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                tokens = TokenObtainPairView().post(request)
                return Response(tokens.data, status=status.HTTP_200_OK)
        return Response({"error": "Usuario o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)

class RegistroView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registro.html'

    def get(self, request):
        form = RegistroForm()
        return Response({'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Crea un nuevo usuario y lo guarda en la base de datos
            # ...
            return redirect('login')
        return Response({'form': form})