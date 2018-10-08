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
    include_package_data=True,
    data_files=[('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_8_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_9_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_10_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_11_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_12_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_13_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_14_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_15_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_17_only.txt']),
                ('data/training_data/iedb/A*01:01', ['data/training_data/iedb/A*01:01/A*01:01_18_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_8_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_9_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_10_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_11_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_12_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_13_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_14_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_15_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_17_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_18_only.txt']),
                ('data/training_data/iedb/A*02:01', ['data/training_data/iedb/A*02:01/A*02:01_30_only.txt'])]
)
