from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


posts = [
    {
        'name': 'Mont blac',
        'user': 'Yessica Cortez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
        'picture': 'http://picsum.photos/200/200/?image=1030'
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
        'picture': 'http://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
        'picture': 'http://picsum.photos/200/200/?image=1077'
    }
]

def list_post(request):
    """listando post existentes"""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <p><figure><img src="{picture}"></figure></p>
            """.format(**post))
    return HttpResponse('<br>'.join(content))
