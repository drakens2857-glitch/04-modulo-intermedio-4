from django.shortcuts import render

from django.http import HttpResponse
def inicio(request):

    return HttpResponse("¡Bienvenido a mi blog!")

def saludo(request, nombre):

    mensaje = f"¡Hola, {nombre}! Bienvenido a mi blog."
    return HttpResponse(mensaje)