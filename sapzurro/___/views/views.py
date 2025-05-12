"""Views Module."""
from django.shortcuts import render
from django.conf import settings

COLORS = {
    'white': '#FFFFFF',
    'black': '#1C1C1C',
    'yellow': '#F1B603',
    'main-1': '#1C4036',
    'main-2': '#3BC2AB',
    'main-3': '#6FAE43',
}


def view_home(request):
    """Home view."""
    context = {
        'foreground_color': COLORS['main-2'],
        'background_color': COLORS['white'],
        'DEBUG': settings.DEBUG,
    }
    return render(request, 'home.html', context)


def view_map(request):
    """Map view."""
    context = {
        'foreground_color': COLORS['yellow'],
        'background_color': COLORS['white'],
        'DEBUG': settings.DEBUG,
    }
    return render(request, 'map.html', context)


def view_about_sapzurro(request):
    """Know About view."""
    context = {
        'foreground_color': COLORS['main-2'],
        'background_color': COLORS['white'],
        'DEBUG': settings.DEBUG,
    }
    return render(request, 'know_about.html', context)


def view_mapaventura(request):
    """Mapaventura view."""
    context = {
        'foreground_color': COLORS['main-3'],
        'background_color': COLORS['white'],
        'DEBUG': settings.DEBUG,

    }
    return render(request, 'know_about.html', context)


def view_about_us(request):
    """About us view."""
    context = {
        'foreground_color': COLORS['white'],
        'background_color': COLORS['black'],
        'DEBUG': settings.DEBUG,
    }
    return render(request, 'know_about.html', context)
