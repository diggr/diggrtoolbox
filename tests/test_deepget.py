#!/usr/bin/env python3

import diggrtoolbox as dt


ENTRY = {'data' : {'raw': {'key1': 'value1',
                           'key2': 'value2'}}}
KEY2 = ['data', 'raw', 'key2']
RAW = ['data', 'raw']
DATA = ['data']

def test_deepget():
    assert dt.deepget(ENTRY, KEY2) == "value2"
    assert dt.deepget(ENTRY, RAW) == {'key1': 'value1', 'key2': 'value2'}
    assert dt.deepget(ENTRY, DATA) == ENTRY['data']
