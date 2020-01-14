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
def config_data():
    """
    Wraps the opening of the zipfile as fixture.
    """
    return dt.Configgr(CONFIG_FILENAME)


def test_configgr_init(config_data):
    assert isinstance(config_data, dt.Configgr)


def test_constant_overwrite(config_data):
    assert config_data['CONSTANT_1'] != CONSTANT_1
