# -*- coding: utf-8 -*-
from setuptools import setup
import djangocms_social

import os


VERSION = djangocms_social.__version__
AUTHOR = djangocms_social.__author__
NAME = 'djangocms-social'
URL = 'https://github.com/pascalmouret/djangocms-social'
AUTHOR_MAIL = 'pascal.mouret@divio.ch'
DESCRIPTION = 'Social plugin for django-cms.'
README = 'README.md'

REQUIREMENTS = [
	'django-filer',
	'django-social-tags',
]

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

# make it work
if not 'a' in VERSION and not 'b' in VERSION: CLASSIFIERS.append('Development Status :: 5 - Production/Stable')
elif 'a' in VERSION: CLASSIFIERS.append('Development Status :: 3 - Alpha')
elif 'b' in VERSION: CLASSIFIERS.append('Development Status :: 4 - Beta')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_MAIL,
    description=DESCRIPTION,
    long_description=read(README),
    url=URL,
    classifiers=CLASSIFIERS,
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    packages=['djangocms_social', 'djangocms_social.models', 'djangocms_social.migrations'],
    include_package_data=True,
    zip_safe=False
)