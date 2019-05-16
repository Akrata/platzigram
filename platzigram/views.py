
from django.http import HttpResponse

import json

from datetime import datetime



def hello_world(request):

    return HttpResponse('la fecha es de hoy es :{now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hs')
        ))


def sort_int(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Ordenados correctamente'
    }
    
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type = 'application/json')


def say_hi(request, name, age):
    if age < 15:
        message = 'Perdon {}, no puedes ingresar aqui por tu edad'.format(name)
    else:
        message = 'Hola {}, bienvenido'.format(name)
    return HttpResponse(message)

    