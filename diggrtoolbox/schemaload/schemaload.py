#!/usr/bin/env python3
"""
Provides two methods which combine opening files and verification against
given schema.
"""

import json
import sys
from jsonschema import validate, ValidationError


def schema_load(data_filename, schema_filename):
    """
    Opens the given file and returns its content as
    python object, if it contains valid JSON data.
    Otherwise exceptions are raised, which need to be
    catched in the calling function
    :param data_filename: full path to the input file
    :param schema_filename: full path to the input file
    :return: dict or list
    """
    with open(schema_filename) as schemafile:
        schema = json.load(schemafile)
    with open(data_filename) as infile:
        data = json.load(infile)
    try:
        validate(data, schema)
    except ValidationError:
        raise
    return data


def load_file_with_schema(filename, schema):
    """
    Loads data from a file and exits the program if errors occur.
    If this functionality is not required please use the schema_load function.
    :param filename: filename of the file with the data
    :param schema: filename of the file with the schema
    :return: the data in the datafile as python object (list or dict)
    """
    try:
        data = schema_load(filename, schema)
    except FileNotFoundError:
        print("sample file or schema file not found. Exiting")
        sys.exit(1)
    except json.decoder.JSONDecodeError as e:
        print("Input File contains errors: {}".format(e))
        sys.exit(1)
    except ValidationError:
        print("Input File is not compliant with the schema.")
        sys.exit(1)
    return data
