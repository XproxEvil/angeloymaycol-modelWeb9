from django import template

register = template.Library()

@register.filter
def format_number(value):
    return '{:,.2f}'.format(value).replace(',', 'X').replace('.', ',').replace('X', '.')
