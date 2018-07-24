#!/usr/bin/env python3
"""
TreeHash is a Function enabling the user to compare nested dicts and lists
by generating a hash.
"""

import hashlib
import json

def treehash(var):
    """
    Returns the hash of any dict or list, by using a string conversion
    via the json library.
    """
    return hashlib.sha256(json.dumps(var, sort_keys=True)
                  .encode("utf-8")).hexdigest()
