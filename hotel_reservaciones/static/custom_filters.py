from django import template

register = template.Library()

@register.filter
def is_available(value):
    return [room for room in value if not room.is_available]