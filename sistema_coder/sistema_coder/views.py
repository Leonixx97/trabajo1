
from django.http import HttpResponse

# Request: Para realizar peticiones.
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista:
def bienvenida(request): # Pasamos un objeto de tipo request como primer argumento.
    return HttpResponse("hola que tal profe?.")

def  bienvenidaRojo(request): #Pasamos un objeto de tipo request como primer argumento.
    return HttpResponse("<p style='color: red;'> Bienvenido a Coder House. =)</p>")