from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from fontawesome.fields import IconField


@python_2_unicode_compatible
class GoodWidget(models.Model):
    title = models.CharField(max_length=100)
    icon = IconField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class SpecificWidget(models.Model):
    title = models.CharField(max_length=100)
    icon = IconField(only_ids=['music', 'heart', 'star'])

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ExcludeWidget(models.Model):
    title = models.CharField(max_length=100)
    icon = IconField(exclude_ids=['music', 'heart', 'star'])

    def __str__(self):
        return self.title
