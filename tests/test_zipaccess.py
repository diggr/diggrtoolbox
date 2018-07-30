#!/usr/bin/env python3
"""
Test Suite for ZipAccess class and children.
"""

import pytest
import zipfile
import io
import json

import diggrtoolbox as dt

from os import remove

TESTDATA = [{'id': 1234,
             'name': 'first_entry'},
            {'id': 1235,
             'name': 'second_entry'},
            {'id': 1236,
             'name': 'third_entry'}]

SUBDATA_1 = {'data': 'additional data for first_entry'}
SUBDATA_2 = {'data': 'additional data for second_entry'}
SUBDATA_3 = {'data': 'additional data for third_entry'}

ZIPFILENAME = "diggrtoolbox_test.zip"


def setup_module():
    mf = io.BytesIO()

    with zipfile.ZipFile(mf, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:

        zf.writestr('data.json', str.encode(json.dumps(TESTDATA), 'utf-8'))
        zf.writestr('subdata/1234.json', str.encode(json.dumps(SUBDATA_1), 'utf-8'))
        zf.writestr('subdata/1235.json', str.encode(json.dumps(SUBDATA_2), 'utf-8'))
        zf.writestr('subdata/1236.json', str.encode(json.dumps(SUBDATA_3), 'utf-8'))

    with open(ZIPFILENAME, "wb") as f:
        f.write(mf.getvalue())


def teardown_module():
    """
    Deletes the temporary file after all tests were run.
    """
    remove(ZIPFILENAME)


@pytest.fixture
def get_zipped_data():
    """
    Wraps the opening of the zipfile as fixture.
    """
    return dt.ZipMultiAccess(ZIPFILENAME)


def test_zipfile():
    """
    Test general opening and accessing functionality of the ZipMultiAccess
    class.
    """
    z = get_zipped_data()
    j = z.json()
    assert TESTDATA == j
    assert z[1234] == SUBDATA_1
    assert z['1234'] == SUBDATA_1
