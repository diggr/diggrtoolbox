import pytest
import diggrtoolbox as dt

def test_platform_mapper():
    """
    Test PlatformMapper class
    """
    gf = dt.PlatformMapper("gamefaqs")
    assert gf.std("gba") == "Nintendo Game Boy Advance"
    assert gf["gibberish"] == None