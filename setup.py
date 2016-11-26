#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='django-videofield',
    version='0.1.0',
    description='Support for video upload in Django models',
    long_description=long_description,
    author='André Luiz',
    author_email='contato@xdvl.info',
    url='https://github.com/dvl/django-videofield',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='django video model field',
    packages=find_packages(),
    test_suite='tests',
)
