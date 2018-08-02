#!/usr/bin/env python3

import yaml
import pytest
import diggrtoolbox as dt

from os import remove

CONSTANT_1 = "constant_1 defined in the program"
CONSTANT_2 = "constant_2 defined in the program"

TEST_CONFIG = { 'constant_1': 'constant_1 defined in the config',
                'constant_3': 'constant_3 defined in the config'}

CONFIG_FILENAME = "test_config.yaml"


def setup_module():
    with open(CONFIG_FILENAME, 'w') as config_file:
        config_file.write(yaml.dump(TEST_CONFIG, default_flow_style=False))


def teardown_module():
    """
    Deletes the temporary file after all tests were run.
    """
    remove(CONFIG_FILENAME)


@pytest.fixture
def get_config_data():
    """
    Wraps the opening of the zipfile as fixture.
    """
    return dt.Configgr(CONFIG_FILENAME)


def test_configgr_init():
    c = get_config_data()
    assert isinstance(c, dt.Configgr)


def test_constant_overwrite():
    c = get_config_data()
    assert c['CONSTANT_1'] != CONSTANT_1


# def test_constant_passthrough():
#     c = get_config_data()
#     print(c.config)
#     assert c['CONSTANT_2'] == CONSTANT_2
