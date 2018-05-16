from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html, mark_safe

register = template.Library()

@register.simple_tag
def fontawesome_icon(icon, weight, title='', large=False, fixed=False, spin=False, li=False,
    rotate=False, border=False, color=False):
    return mark_safe('<i title="{title}" class="{weight} fa-{icon}{large}{fixed}{spin}{li}{rotate}{border}" {color}></i>'.format(
        title=title,
        weight=weight,
        icon=icon,
        large=' fa-lg' if large is True else '',
        fixed=' fa-fw' if fixed else '',
        spin=' fa-spin' if spin else '',
        li=' fa-li' if li else '',
        rotate=' fa-rotate-%s' % str(rotate) if rotate else '',
        border=' fa-border' if border else '',
        color='style="color:%s;"' % color if color else ''
    ))

@register.simple_tag
def fontawesome_stylesheet():
    href = getattr(settings, 'FONTAWESOME_CSS_URL', static('fontawesome/css/font-awesome.min.css'))
    link_body = ''
    if href.endswith('.js'):
        link_body = '<script defer src="{0}"></script>'
    else:
        link_body = '<link href="{0}" rel="stylesheet" media="all">'
    link = format_html(link_body, href)
    return link
