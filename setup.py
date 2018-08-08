#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
diggrtoolbox

Copyright (C) 2018 Leipzig University Library <info@ub.uni-leipzig.de>

@author   F. Rämisch <raemisch@ub.uni-leipzig.de>
@author   P. Mühleder <muehleder@ub.uni-leipzig.de>
@license  https://opensource.org/licenses/MIT MIT License
 
Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup, find_packages
from os.path import dirname, abspath, join

base_path = dirname(abspath(__file__))

with open(join(base_path, "README.rst")) as readme_file:
    readme = readme_file.read()

with open(join(base_path, "requirements.txt")) as req_file:
    requirements = req_file.readlines()

setup(
    name = "diggrtoolbox",
    description = "diggrtoolbox provides a variety of tools to be used in "
                  "game research and the digital humanities in general.",
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
