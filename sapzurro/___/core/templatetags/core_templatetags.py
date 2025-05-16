from django import template
from core.models import Carousel, ShouldKnowSection

register = template.Library()


@register.inclusion_tag("shared/carousel.html")
def get_carousel(carousel_name):
    carousel = Carousel.objects.get(name=carousel_name)
    return {
        'images': carousel.get_context_fields(),
        'show_description': carousel.show_description,
    }

@register.inclusion_tag("shared/know_about_section.html")
def get_know_about_sections():
    return {
        'sections': ShouldKnowSection.objects.all()
    }
