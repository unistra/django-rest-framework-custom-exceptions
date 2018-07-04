#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


with open('README.rst') as readme:
    long_description = readme.read()


with open('requirements.txt') as requirements:
    lines = requirements.readlines()
    libraries = [lib for lib in lines if not lib.startswith('-')]
    dependency_links = [link.split()[1] for link in lines if
        link.startswith('-f')]


setup(
    name='djangorestframework-custom-exceptions',
    version='1.0.2',
    packages=find_packages(),
    install_requires=libraries,
    dependency_links=dependency_links,
    long_description=long_description,
    author='Morgan Bohn',
    author_email='morgan.bohn@unistra.fr',
    maintainer='Morgan Bohn',
    maintainer_email='morgan.bohn@unistra.fr',
    description='Custom exceptions for Django REST Framework',
    keywords=['django', 'REST', 'rest_framework', 'exceptions'],
    url='https://github.com/unistra/django-rest-framework-custom-exceptions',
    download_url='https://pypi.python.org/pypi/djangorestframework-custom-exceptions',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ]
)
