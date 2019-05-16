from django.shortcuts import render

from datetime import datetime

# Create your views here.


posts = [
    {
        'title':'Mont blac',
        'user': {
            'name': 'Yésica Cortes',
            'picture': 'http://picsum.photos/60/60/?image=1027' 
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
        'photo': 'http://picsum.photos/200/200/?image=1036'
    },
      {
        'title':'Via Lactea',
        'user': {
            'name': 'Christian v.Hesent',
            'picture': 'http://picsum.photos/60/60/?image=1005' 
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
        'photo': 'http://picsum.photos/200/200/?image=903'
    },
    {
        'title':'Nuevo auditorio',
        'user': {
            'name': 'Uriel',
            'picture': 'http://picsum.photos/60/60/?image=883' 
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
        'photo': 'http://picsum.photos/200/200/?image=1076'
    }
]

def list_post(request):
    """listando post existentes"""
    
    return  render(request, 'feed.html', {'posts': posts})
