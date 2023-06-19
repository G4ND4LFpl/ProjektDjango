from django import template
from django.templatetags.static import static
register = template.Library()

@register.simple_tag
def load_img(img, *args, **kwargs):
    """Returns the img url of the given img

    .. usage::  {% get_img_url image_object %}

    """
    #image_path = 'here you build your path using the img passed'
    return static(img)