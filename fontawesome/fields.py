from django.db import models
from django.utils.translation import ugettext as _

from . import Icon
from .forms import IconFormField


class IconField(models.Field):

    description = _('A fontawesome icon field')
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 60
        kwargs['blank'] = True

        self.only_ids = kwargs.pop('only_ids', [])
        self.exclude_ids = kwargs.pop('exclude_ids', [])

        super(IconField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def to_python(self, value):
        if not value or value == 'None':
            return None

        if isinstance(value, Icon):
            return value

        # default => string
        return Icon(id=value)

    def get_prep_value(self, value):
        return str(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': IconFormField,
        }

        defaults.update(kwargs)
        defaults.update({
            'only_ids': self.only_ids,
            'exclude_ids': self.exclude_ids
        })
        return super(IconField, self).formfield(**defaults)
