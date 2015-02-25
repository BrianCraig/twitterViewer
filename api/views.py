from django.shortcuts import render
from .events import user, search
from django.http import JsonResponse, HttpResponse
# Create your views here.

def get_user(request, username):
    response = user(username)
    json = JsonResponse(response._json, safe=False)
    return HttpResponse(json)


def get_search(request, query):
    tweets = search(query,request.GET['lat'],request.GET['lng'],request.GET['km'])
    # json = JsonResponse(response._json,safe=False)
    respuesta = []
    for x in tweets:
        resumen = {
            'tweet': x.text,
            'id_tweet': x.id,
            'usuario': x.user.screen_name,
            'usuario_nombre': x.user.name,
            'usuario_imagen': x.user.profile_image_url,
            'coordenadas': x.coordinates['coordinates'][::-1],
        }

        respuesta.append(resumen)

    return HttpResponse(JsonResponse(respuesta,safe=False))