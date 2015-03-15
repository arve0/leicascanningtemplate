#!/usr/bin/env python

import os
import sys
from setuptools import setup


os.system('make rst')
readme = open('README.rst').read()

setup(
    name='leicascanningtemplate',
    version=open(os.path.join('leicascanningtemplate', 'VERSION')).read().strip(),
    description='convenience library for talking with leica matrix screener scanning templates',
    long_description=readme,
    author='Arve Seljebu',
    author_email='arve.seljebu@gmail.com',
    url='https://github.com/arve0/leicascanningtemplate',
    packages=[
        'leicascanningtemplate',
    ],
    package_dir={'leicascanningtemplate': 'leicascanningtemplate'},
    package_data={'leicascanningtemplate': ['VERSION']},
    include_package_data=True,
    install_requires=[
        'lxml'
    ],
    license='MIT',
    zip_safe=False,
    keywords='leicascanningtemplate',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
