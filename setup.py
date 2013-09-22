#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pyzufall.version import __version__
from pyzufall import __doc__

setup(
    name='PyZufall',
    version=__version__,
    url='https://pyzufall.readthedocs.org',
    license='GPLv3',
    author='davidak',
    author_email='post@davidak.de',
    packages=['pyzufall'],
    package_dir={'pyzufall': 'pyzufall'},
    package_data={'pyzufall': ['data/*.txt']},
    platforms='any',
    description=__doc__,
    long_description=open('README.rst').read(),
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: German',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Artistic Software',
        'Topic :: Games/Entertainment',
        'Topic :: Text Processing :: Linguistic',
    ],
    zip_safe=False,
)