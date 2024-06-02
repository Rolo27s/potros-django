from django.shortcuts import render
from django.http import JsonResponse
from potros.models import Noticias, Calendario, Equipo, Instagram

MSG_ERROR_HTTP = "Unsuported HttpMethods"

# Navegacion desde la pagina principal hasta las diferentes opciones
def home(request):
    return render(request, 'home.html')

def noticias(request):
    return render(request, 'potros/noticias.html')

def calendario(request):
    return render(request, 'potros/calendario.html')

def equipo(request):
    return render(request, 'potros/equipo.html')

def instagram(request):
    return render(request, 'potros/instagram.html')


#Endpoints
def get_all_noticias(request):
    if request.method != 'GET':
        return JsonResponse({'error':MSG_ERROR_HTTP}, status = 405) 
        # El servidor rechaza el acceso a un recurso (URI) debido a restricciones del método HTTP

    noticias = Noticias.objects.all().order_by('-fecha')

    response = []

    for noticia in noticias:
        response.append(noticia.to_json())

    return JsonResponse(response, safe=False, status = 200)

def get_calendario(request):
    if request.method != 'GET':
        return JsonResponse({'error':MSG_ERROR_HTTP}, status = 405) 
        # El servidor rechaza el acceso a un recurso (URI) debido a restricciones del método HTTP

    calendario = Calendario.objects.all().order_by('fecha')

    response = []

    for dia_partido in calendario:
        response.append(dia_partido.to_json())

    return JsonResponse(response, safe=False, status = 200)

def get_equipo(request):
    if request.method != 'GET':
        return JsonResponse({'error':MSG_ERROR_HTTP}, status = 405) 
        # El servidor rechaza el acceso a un recurso (URI) debido a restricciones del método HTTP

    equipo = Equipo.objects.all().order_by('dorsal')

    response = []

    for jugador in equipo:
        response.append(jugador.to_json())

    return JsonResponse(response, safe=False, status = 200)

def get_instagram(request):
    if request.method != 'GET':
        return JsonResponse({'error':MSG_ERROR_HTTP}, status = 405) 
        # El servidor rechaza el acceso a un recurso (URI) debido a restricciones del método HTTP

    instagram = Instagram.objects.all()

    response = []

    for imagen in instagram:
        response.append(imagen.to_json())

    return JsonResponse(response, safe=False, status = 200)