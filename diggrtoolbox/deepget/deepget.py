#!/usr/bin/env python3
"""
Deepget is a small function enabling the user to "cherrypick" specific values
from deeply nested dicts or lists.

Author: Florian Rämisch <raemisch@ub.uni-leipzig.de>
Copyright: Universitätsbibliothek Leipzig, 2018
License: GPLv3
"""


def deepget(obj, keys):
    """
    Deepget is a small function enabling the user to "cherrypick" specific
    values from deeply nested dicts or lists. This is useful, if the just one
    specific value is needed, which is hidden in multiple hierarchies.

    :Example:

        >>> import diggrtoolbox as dt
        >>> ENTRY = {'data' : {'raw': {'key1': 'value1',
                                       'key2': 'value2'}}}
        >>> KEY2 = ['data', 'raw', 'key2']
        >>> dt.deepget(ENTRY, KEY2) == 'value2'
        True
    """
    def deeper(obj, keys):
        if len(keys) > 1:
            return deeper(obj[keys.pop(0)], keys)
        else:
            return obj[keys.pop(0)]
    return deeper(obj, keys.copy())
