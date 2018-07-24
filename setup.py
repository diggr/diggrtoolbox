#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    # setup_requires=['setup.cfg'],
    setup_cfg=True
)
