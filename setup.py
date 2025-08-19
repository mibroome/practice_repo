#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name="practice_code",
    version="1.0",
    author='Madelyn Broome',
    author_email='mabroome@ucsc.edu',
    description="Practice repo for group meeting",
    install_requires=[line.strip() for line in
                      open('requirements.txt', 'r').readlines()],
    packages=find_packages(),
    include_package_data=True,
)