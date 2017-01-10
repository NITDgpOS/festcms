from django import template
from django.core.urlresolvers import resolve, Resolver404

from festflow.models import NavbarEntry

register = template.Library()

@register.inclusion_tag('festflow/navbar.html', takes_context=True)
def navbar(context):
    return {
        'entries': NavbarEntry.objects.all()
    }
