from django import template
from core.models import Carousel

register = template.Library()


@register.inclusion_tag("shared/carousel.html")
def get_carousel(carousel_name):
    return {
        'images': Carousel.objects.get(name=carousel_name).get_image_urls()
    }
