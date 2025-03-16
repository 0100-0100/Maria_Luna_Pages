from django.shortcuts import render
from django.conf import settings
from django.templatetags.static import static
import os


colors = {
    'white': '#FFF7D8',
    'black': '#1C1C1C',
    'main-1': '#1C4036',
    'main-2': '#3BC2AB',
    'main-3': '#6FAE43',
    'yellow': '#F1B603'
}


# Create your views here.
def home(request):
    context = {
        'foreground_color': colors['yellow'],
        'background_color': colors['main-1']
    }
    carousel_path = 'carousel-1'
    image_dir = os.path.join(settings.MEDIA_URL, carousel_path)
    image_files = [
        {'url': f'{settings.MEDIA_URL}{carousel_path}/{filename}'}
        for filename in os.listdir(os.path.join(settings.MEDIA_ROOT, carousel_path))
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))
    ]
    context.update({
        'images': image_files
    })
    return render(request, 'home.html', context)


def map_view(request):
    context = {
        'foreground_color': colors['main-2'],
        'background_color': colors['black']
    }
    return render(request, 'map.html', context)
