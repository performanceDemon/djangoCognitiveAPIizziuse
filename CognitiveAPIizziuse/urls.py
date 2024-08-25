from django.urls import path
from .views import MiVista, LoginView , RegistroView, CognitiveHomeView

urlpatterns = [
    path('', MiVista.as_view()),
    path('mi-vista/', MiVista.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('cognitive_home/', CognitiveHomeView.as_view(), name='cognitive_home'),
]