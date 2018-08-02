#!/usr/bin/env python3

import diggrtoolbox as dt

from copy import deepcopy

TESTDICT = {'key0': 'value0',
            'key1': 'value2',
            'key2': 'value2',
            'key3': 'value3',
            'key4': {'subkey0': 'subvalue0',
                     'subkey1': 'subvalue1', },
            'key5': ['sublistelement0',
                     'sublistelement1',
                     'sublistelement2',
                     'This is a more complicated entry to find.'],
            'key6': 'value6',
            'key7': [{'sublistkey0': ['sublistvalueelement0',
                                      'sublistvalueelement1',
                                      'sublistvalueelement2'],
                      'sublistkey1': 'sublistvalue1', },
                     {'sublistkey2': ['sublistvalueelement3',
                                      'sublistvalueelement4',
                                      'sublistvalueelement5'],
                      'sublistkey3': 'sublistvalue3', },
                     {'sublistkey4': ['sublistvalueelement6',
                                      'sublistvalueelement7',
                                      'sublistvalueelement8'],
                      'sublistkey5': 'sublistvalue5',
                      'sublistkey6': 6},
                     7,
                     8,
                     9],
            'key8': [1, 2, 3, 4]}

TESTDICT_NO_ID = TESTDICT.copy()
TESTDICT_NO_ID.pop('key0')

TESTLIST_ONE = [TESTDICT]

TESTLIST_MULTI_SAME = [TESTDICT for i in range(5)]

TESTLIST_MULTI_DIFFERENT = [TESTDICT for i in range(4)] + [TESTDICT_NO_ID]

FIND_HIDDEN_VALUE = (('sublistvalueelement5', ['key7', 1, 'sublistkey2', 2]),
                     ('sublistvalue5', ['key7', 2, 'sublistkey5']),
                     ('sublistelement2', ['key5', 2]),
                     ('complicated', ['key5', 3]),
                     ('sublistkey0', ['key7', 0, 'sublistkey0']),
                     (7, ['key7', 3]))


def test_search():
    """
    Test if the search function works properly
    """
    tree = dt.TreeExplore(deepcopy(TESTDICT))
    for e, (term, path) in enumerate(FIND_HIDDEN_VALUE):
        results = tree.search(term)
        for step in path:
            print(step, end=", ")
        print()
        assert path == results[0]['route']
