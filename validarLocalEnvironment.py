import os

# Definir la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoCognitiveAPIizziuse.settings')

from django.conf import settings

class ValidarAmbiente:
    def imprimir_variables_entorno(self):
        print(settings.DATABASES['default']['HOST'])
        print(settings.DATABASES['default']['PORT'])
        print(settings.DATABASES['default']['NAME'])
        print(settings.DATABASES['default']['USER'])
        print(settings.DATABASES['default']['PASSWORD'])

# Crear una instancia de la clase
validar_ambiente = ValidarAmbiente()

# Llamar a la función
validar_ambiente.imprimir_variables_entorno()