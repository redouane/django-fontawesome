==================
django-fontawesome
==================

.. image:: https://badge.fury.io/py/django-fontawesome.svg
    :target: http://badge.fury.io/py/django-fontawesome

.. image:: https://pypip.in/download/django-fontawesome/badge.png
    :target: https://pypi.python.org/pypi/django-fontawesome/
    :alt: Downloads

.. image:: https://pypip.in/license/django-fontawesome/badge.png
    :target: https://pypi.python.org/pypi/django-fontawesome/
    :alt: License

PS: still under developement, things may change, once stable it will be on PyPI.

django-fontawesome is a django app that provides a couple of fontawesome/django related utilities, namely:

- an IconField to associate fontawesome icons with model instances
- templatetags to render fontawesome icons

also included:

- admin support for the IconField
- fr locale translation


Requirements
============

- PyYAML
- Select2 (included)
- JQuery (uses django's jquery in admin panel)


Settings
========
you need to tell django-fontawesome where your font-awesome.css resides using::

    FONTAWESOME_CSS_URL # default is 'css/font-awesome.min.css'


you can also tell it the fontawesome prefix, which as of right now is 'fa', using::

    FONTAWESOME_PREFIX # default is 'fa'


Installation / Usage
====================

1. add 'fontawesome' to your installed apps setting like this::

    INSTALLED_APPS = (
        ...
        'fontawesome',
    )

2. import and use the iconfield::
    
    from fontawesome.fields import IconField


    class Category(models.Model):
        ...
        icon = IconField()


here's what the widget looks like in the admin panel:

|admin-widget|

3. you can then render the icon in your template like this::
    
    {% for category in categories.all %}
        {% if category.icon %}
            {{ category.icon.as_html }}
        {% endif %}
    {% endfor %}


4. you can also use the provided template tag to render icons::

    {% load fontawesome %}
     
    {% fontawesome_icon 'user' %}

    {% fontawesome_icon 'star' large=True spin=True %}


5. profit!!!

.. |admin-widget| image:: docs/images/admin-widget.png
