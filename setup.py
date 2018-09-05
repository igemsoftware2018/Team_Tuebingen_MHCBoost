#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.1dev'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='mhc-1',
    version=version,
    description='MHC class I binding predictor',
    long_description=readme,
    keywords=['mhc-1'],
    author='iGEM 2018',
    author_email='igem@ifib.uni-tuebingen.de',
    license=license,
    scripts=['scripts/mhc-1'],
    install_requires=required,
    packages=find_packages(exclude='docs'),
    include_package_data=True
)
