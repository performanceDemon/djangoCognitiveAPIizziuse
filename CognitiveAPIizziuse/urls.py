from django.urls import path
from .views import MiVista, LoginView , RegistroView

urlpatterns = [
    path('', MiVista.as_view()),
    path('mi-vista/', MiVista.as_view()),
    path('login/', LoginView.as_view()),
    path('registro/', RegistroView.as_view(), name='registro'),
]