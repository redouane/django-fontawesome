import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fontawesome',
    version='0.2.5',
    packages=['fontawesome'],
    include_package_data=True,
    license='BSD License',
    description='a django app that provides a couple of fontawesome/django related utilities.',
    long_description=README,
    url='https://www.github.com/redouane/django-fontawesome',
    author='Redouane Zait',
    author_email='redouanezait@gmail.com',
    install_requires=['PyYAML', 'django'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    zip_safe=False
)
