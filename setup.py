#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.system('make rst')
readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://leicascanningtemplate.rtfd.org."""

setup(
    name='leicascanningtemplate',
    version='0.0.1',
    description='convenience library for talking with leica matrix screener scanning templates',
    long_description=readme + '\n\n' + doclink,
    author='Arve Seljebu',
    author_email='arve.seljebu@gmail.com',
    url='https://github.com/arve0/leicascanningtemplate',
    packages=[
        'leicascanningtemplate',
    ],
    package_dir={'leicascanningtemplate': 'leicascanningtemplate'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='leicascanningtemplate',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
