from django import template

register = template.Library()

@register.filter()
def to_float(value:str)->float:
    return float(value)

