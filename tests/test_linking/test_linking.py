import pytest
import Levenshtein as lev
from diggrtoolbox.linking import link_by_titles
from diggrtoolbox.linking.helpers import std
from diggrtoolbox.linking.config import *

#test linking by titles
@pytest.mark.parametrize(
    "titles1, titles2, output",
    [
        (
            [
                "Resident Evil 2",
                "Biohazard 2"
            ], 
            [
                "Resident Evil 2",
                "RE2"
            ], 1),
        (
            [
                "Resident Evil 2",
                "Biohazard 2"
            ], 
            [
                "Resident Evil",
                "RE"
            ], lev.ratio(std("Resident Evil 2"), std("Resident Evil")) - NUMBERING_WEIGHT),
    ],    
)
def test_linking_by_titles(titles1, titles2, output):
    assert link_by_titles(titles1, titles2) == output