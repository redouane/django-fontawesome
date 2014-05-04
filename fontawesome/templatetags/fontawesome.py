from django import template

register = template.Library()

@register.simple_tag
def fontawesome_icon(icon, large=False, fixed=False, spin=False):

    return '<i class="fa fa-{icon} {large} {fixed} {spin}"></i>'.format(
        icon=icon,
        large='fa-lg' if large is True else '',
        fixed='fa-fw' if fixed else '',
        spin='fa-spin' if spin else '',
    )
