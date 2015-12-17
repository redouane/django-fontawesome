from django import forms
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class IconWidget(forms.Select):

    def render_option(self, selected_choices, option_value, option_label):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''

        return format_html('<option data-icon="{0}" value="{0}"{1}>{2}</option>',
            option_value,
            selected_html,
            force_text(option_label),
        )

    class Media:

        js = (
            'fontawesome/js/django_fontawesome.js',
            'fontawesome/select2/select2.min.js'
        )

        css = {
            'all': (
                getattr(settings, 'FONTAWESOME_CSS_URL', 'fontawesome/css/font-awesome.min.css'),
                'fontawesome/select2/select2.css',
                'fontawesome/select2/select2-bootstrap.css'
            )
        }
