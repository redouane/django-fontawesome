# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.test import TestCase

from fontawesome.utils import get_icon_choices
from .models import GoodWidget, SpecificWidget, ExcludeWidget


class GoodWidgetForm(forms.ModelForm):

    class Meta:
        model = GoodWidget


class SpecificWidgetForm(forms.ModelForm):

    class Meta:
        model = SpecificWidget


class ExcludeWidgetForm(forms.ModelForm):

    class Meta:
        model = ExcludeWidget


class IconFieldTestCases(TestCase):

    def test_all_icons(self):
        all_icons = get_icon_choices()
        good_widget_form = GoodWidgetForm()

        self.assertEqual(all_icons,
            good_widget_form.fields['icon'].widget.choices,
            u"good_widget_form.icon field choices should have the full set of "
            U"icons")

    def test_data_persisted(self):
        widget = GoodWidgetForm({'title': 'Test', 'icon': 'music'}).save()
        self.assertEqual(widget.icon.id, 'music', u'widget.icon should equal '
            u'"music". Instead equals: {}'.format(widget.icon.id))

    def test_only_specific_ids_included(self):
        specific_widget_form = SpecificWidgetForm()

        expected_choices = [
            ('', '----------'),
            ('music', 'Music'),
            ('heart', 'Heart'),
            ('star',  'Star'),
        ]
        actual_choices = specific_widget_form.fields['icon'].widget.choices
        self.assertEqual(actual_choices, expected_choices,
            u"specific_widget_form.icon field choices does not match expected "
            u"choices. Instead was: {}".format(actual_choices))

    def test_only_specific_ids_excluded(self):
        excluded_widget_form = ExcludeWidgetForm()

        excluded_choices = [
            ('music', 'Music'),
            ('heart', 'Heart'),
            ('star',  'Star'),
        ]
        actual_choices = excluded_widget_form.fields['icon'].widget.choices

        for excluded_choice in excluded_choices:
            self.assertFalse(excluded_choice in actual_choices)
