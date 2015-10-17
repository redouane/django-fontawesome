# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.db import models
from django.test import TestCase
from django.utils.encoding import python_2_unicode_compatible

from fontawesome.fields import IconField
from fontawesome.utils import get_icon_choices


@python_2_unicode_compatible
class GoodWidget(models.Model):
    title = models.CharField(max_length=100)
    icon = IconField()

    def __str__(self):
        return self.title


class WidgetForm(forms.ModelForm):

    class Meta:
        model = GoodWidget


@python_2_unicode_compatible
class SpecificWidget(models.Model):
    title = models.CharField(max_length=100)
    icon = IconField(only_ids=['music', 'heart', 'star'])

    def __str__(self):
        return self.title


class SpecificWidgetForm(forms.ModelForm):

    class Meta:
        model = SpecificWidget


@python_2_unicode_compatible
class ExcludeWidget(models.Model):
    title = models.CharField(max_length=100)
    icon = IconField(exclude_ids=['music', 'heart', 'star'])

    def __str__(self):
        return self.title


class ExcludeWidgetForm(forms.ModelForm):

    class Meta:
        model = ExcludeWidget


class IconFieldTestCases(TestCase):

    def test_all_icons(self):
        all_icons = get_icon_choices()
        good_widget_form = WidgetForm()

        self.assertEqual(all_icons,
            good_widget_form.fields['icon'].widget.choices,
            u"good_widget_form.icon field choices should have the full set of "
            U"icons")

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
