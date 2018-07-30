#!/usr/bin/env python3

import diggrtoolbox as dt

from copy import deepcopy

TESTDICT = {'key0': 'value0',
            'key1': 'value1',
            'key2': 'value2',
            'key3': [0, 1, 2, 3],
            'key4': {'subkey0': 'subvalue0',
                     'subkey1': 'subvalue1'}}


def test_deterministic():
    """
    Test if ran multiple times, the same dictionaries yield the same hash.
    """
    dict_1 = deepcopy(TESTDICT)
    dict_2 = deepcopy(TESTDICT)

    for i in range(10):
        assert dt.treehash(dict_1) == dt.treehash(dict_2)


def test_missing_keyvalue_difference():
    """
    Test if different dicts (missing elements/key-value-pairs) yield different
    hashes.
    """
    dict_1 = deepcopy(TESTDICT)
    dict_2 = deepcopy(TESTDICT)

    dict_2.pop('key0')
    for i in range(10):
        assert dt.treehash(dict_1) != dt.treehash(dict_2)

    dict_1.pop('key1')
    for i in range(10):
        assert dt.treehash(dict_1) != dt.treehash(dict_2)


def test_change_value_difference():
    """
    Test if different dicts (changes of signs/elements in values) yield
    different hashes.
    """
    dict_1 = deepcopy(TESTDICT)
    dict_2 = deepcopy(TESTDICT)

    dict_1['key1'] = 'value01'
    for i in range(10):
        assert dt.treehash(dict_1) != dt.treehash(dict_2)

    dict_1 = deepcopy(TESTDICT)
    dict_1['key3'].append(4)
    for i in range(10):
        assert dt.treehash(dict_1) != dt.treehash(dict_2)
