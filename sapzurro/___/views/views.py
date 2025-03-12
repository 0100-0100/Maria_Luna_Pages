from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'foreground_color': '#F8F6E0',
        'background_color': '#275950'
    }
    return render(request, 'home.html', context)


def map_view(request):
    context = {
        'foreground_color': '#275950',
        'background_color': '#F8F6E0'
    }
    return render(request, 'home.html', context)
