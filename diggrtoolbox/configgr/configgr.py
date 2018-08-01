#!/usr/bin/env python3
"""
The Configgr provides a simple and easy to use configuration method.

Author: F. Rämisch <raemisch@ub.uni-leipzig.de>
Copyright: Universitätsbibliothek Leipzig, 2018
License: GNU General Public License v3
"""

import inspect

from yaml import load


class Configgr:
    """
    Developers define a default configuration for their programs using
    constants in the source . These constants are  inspected, upon
    instanciation, and saved into the config object. The config file is read,
    and all settings are imported too. Constants are overwritten in the config,
    out of course are still usable in the program config.

    This results in the fact, that you can set a default behaviour in the
    source code, let the user configure a setting in a config file, but comment
    it out upon shipping, to indicate that configuration of this setting is not
    required.
    """

    def _load_config(self):
        """
        Opens the configuration file and stores its contents in the class.
        """
        with open(self.config_filename) as config_file:
            for var, value in load(config_file).items():
                self.config[var] = value

    def _set_locals(self):
        """
        Inspects the calling frame for any constants (i.e. uppercase variables)
        and puts them into the config (but referenced lowercase).
        """
        frame = inspect.currentframe()
        caller_locals = frame.f_back.f_back.f_locals

        for local_var_name, local_var_value in caller_locals.items():
            if local_var_name.isupper():
                self.config[local_var_name.lower()] = local_var_value

    def __init__(self,
                 config_filename,
                 inspect_locals=True,
                 try_lower_on_fail=True):
        """
        Initializes the Config class.

        :param config_filename: path to the configuration file.
        :param inspect_locals: If the locals of the caller should be put into
                               the config. Default: True
        :param try_lower_on_fail: Tries to return a lower case variable
                                  from the config, if the requested variable is
                                  uppercase and a lower case variant is there.
                                  Default: True
        """
        self.config_filename = config_filename
        self.config = dict()

        if inspect_locals:
            self._set_locals()

        self._load_config()

    def __getitem__(self, item_key):
        """
        Returns the correct object from the config, or a item_constant
        if the requested object is not configured.

        :param item_key: name/identifier/key of the config object
        """
        if item_key in self.config.keys():
            return self.config[item_key]
        elif item_key.isupper() and item_key.lower() in self.config.keys():
            return self.config[item_key.lower()]
        else:
            raise KeyError("Not found.")
