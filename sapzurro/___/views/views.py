from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'foreground_color': '#3BC2AB',
        'background_color': '#1C4036'
    }
    return render(request, 'home.html', context)


def map_view(request):
    context = {
        'foreground_color': '#275950',
        'background_color': '#1C4036'
    }
    return render(request, 'home.html', context)
