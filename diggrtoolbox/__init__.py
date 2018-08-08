#!/usr/bin/env python3
"""
diggrtoolbox is the main package around all the small tools which were
developed in the diggr group. Each tool is located in a separated subpackage.

All tools are made available at package level, as every subpackage often only
contains one class/function, separation into the subpackages appeared to be
not the best idea.

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


from .configgr import Configgr
from .deepget import deepget
from .treeexplore import TreeExplore, treehash
from .zipaccess import ZipSingleAccess, ZipMultiAccess, ZipListAccess
from .standardize import remove_html, remove_bracketed_text, remove_punctuation, std_url, std
from .platform_mapping import PlatformMapper
from .linking import link_by_titles

__all__ = ['Configgr',
           'deepget',
           'link_by_titles',
           'PlatformMapper',
           'TreeExplore',
           'treehash',
           'ZipSingleAccess',
           'ZipMultiAccess',
           'ZipListAccess']
