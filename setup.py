#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
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
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    install_requires=['future'],
    tests_require=['nose>=1.0', 'coverage'],
    test_suite='nose.collector',
    classifiers=[
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.0',
        #'Programming Language :: Python :: 3.1',
        #'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        #'Programming Language :: Python :: Implementation :: IronPython',
        #'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: PyPy',
        #'Programming Language :: Python :: Implementation :: Stackless',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: German',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Topic :: Artistic Software',
        'Topic :: Games/Entertainment',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    zip_safe=False,
)
