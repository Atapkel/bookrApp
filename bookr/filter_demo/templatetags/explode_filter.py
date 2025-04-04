from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def explode(value, seperator):
    return value.split(seperator)
