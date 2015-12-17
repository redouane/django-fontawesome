from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext as _

from . import Icon
from .widgets import IconWidget
from .utils import get_icon_choices


class IconFormField(forms.Field):

    def __init__(self, *args, **kwargs):
        self.only_ids = kwargs.pop('only_ids', [])
        self.exclude_ids = kwargs.pop('exclude_ids', [])

        if self.only_ids and self.exclude_ids:
            raise ImproperlyConfigured(_('IconFormField kwargs accepts values '
                'for "only_ids" or "exclude_ids", but not both.'))

        if 'initial' in kwargs:
            kwargs['initial'] = Icon(*kwargs['initial'])

        override_widget = kwargs.get('widget')

        fontawesome_prefix = getattr(settings, 'FONTAWESOME_PREFIX', 'fa')

        css_classes = ['fontawesome-select']
        attrs = {
            'class': '',
            'data-fontawesome-prefix': fontawesome_prefix,
        }

        if override_widget and override_widget.attrs:
            css_classes += override_widget.attrs.get('class', '').split()

        attrs['class'] = ' '.join(css_classes)

        self.widget = IconWidget(attrs)
        self.widget.choices = get_icon_choices(only_ids=self.only_ids,
            exclude_ids=self.exclude_ids)

        super(IconFormField, self).__init__(*args, **kwargs)
