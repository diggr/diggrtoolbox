#!/usr/bin/env python3
"""
diggrtoolbox is the main package around all the small tools which were
developed in the diggr group. Each tool is located in a separated subpackage.

All tools are made available at package level, as every subpackage often only
contains one class/function, separation into the subpackages appeared to be
not the best idea.
"""

from .deepget import deepget
from .treeexplore import TreeExplore, treehash
from .zipaccess import ZipSingleAccess, ZipMultiAccess, ZipListAccess
from .standardize import remove_html, remove_bracketed_text, remove_punctuation, std_url, std


__all__ = ['deepget',
           'TreeExplore',
           'treehash',
           'ZipSingleAccess',
           'ZipMultiAccess',
           'ZipListAccess']
