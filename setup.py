#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import dirname, abspath, join

base_path = dirname(abspath(__file__))

with open(join(base_path, "README.rst")) as readme_file:
    readme = readme_file.read()

with open(join(base_path, "requirements.txt")) as req_file:
    requirements = req_file.readlines()

setup(
    name = "diggrtoolbox",
    description = "diggrtoolbox provides a variety of tools to be used in game research and the digital humanities in general.",
    long_description=readme,
    license="GPL",
    author = "Diggr Team",
    author_email='team@diggr.link',
    url='https://github.com/diggr/diggrtoolbox',
    packages=find_packages(exclude=['dev', 'docs']),
    package_dir={
            'diggrtoolbox': 'diggrtoolbox'
        },
    version = "0.2",
    install_requires=requirements,
    test_suite="pytest",
    include_package_data=True,
)
