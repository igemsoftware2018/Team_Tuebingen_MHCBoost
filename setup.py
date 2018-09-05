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
    name='template',
    version=version,
    description='Template for python based projects',
    long_description=readme,
    keywords=['test'],
    author='Lukas Heumos',
    author_email='lukas.heumos@gmail.com',
    license=license,
    scripts=['scripts/template'],
    install_requires=required,
    packages=find_packages(exclude='docs'),
    include_package_data=True
)
