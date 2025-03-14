from django.shortcuts import render
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
        'foreground_color': colors['main-1'],
        'background_color': colors['white']
    }
    return render(request, 'home.html', context)


def map_view(request):
    context = {
        'foreground_color': colors['main-2'],
        'background_color': colors['black']
    }
    return render(request, 'map.html', context)
