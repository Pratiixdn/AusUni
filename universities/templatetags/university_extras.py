"""
Custom template filters for the AusUni universities app.
"""
from django import template

register = template.Library()


@register.filter
def split(value, delimiter=','):
    """
    Split a string by a delimiter and return a list of stripped items.
    Usage: {{ value|split:", " }}  or  {% for x in value|split:", " %}
    """
    if not value:
        return []
    return [item.strip() for item in value.split(delimiter)]
