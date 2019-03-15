from django.conf import settings
from django.utils.html import format_html

class Icon(object):

    def __init__(self, id):
        self.id = id

    def as_html(self):
        if not self.id:
            return ''

        return format_html('<i class="{0}"></i>', self.css_class, self.id)

    @property
    def css_class(self):
        return '{0} {0}-{1}'.format(self.prefix, self.id)

    @property
    def prefix(self):
        return getattr(settings, 'FONTAWESOME_PREFIX', 'fa')

    def __str__(self):
        return self.id

    def __unicode__(self):
        return str(self)