import pytest
import diggrtoolbox as dt


@pytest.mark.parametrize("input_string,expected",[
    ("<b>ABC</b>", "ABC"),
    ("", ""),
    (None, None),
    ("der <i> abc", "der abc")
])
def test_remove_html(input_string, expected):
    """
    Test removing html tags.
    """
    assert dt.remove_html(input_string) == expected


@pytest.mark.parametrize("input_string,expected", [
    ("Yada.", "Yada"),
    ("yasd", "yasd"),
    (None, None),
    (".:!", ""),
    ("", "")
])
def test_remove_punctuation(input_string, expected):
    """
    Test removing punctuation from string.
    """
    assert dt.remove_punctuation(input_string) == expected


@pytest.mark.parametrize("input_string, expected", [
    ("test (Test)", "test"),
    ("brackets (in [brackets])", "brackets")
])
def test_remove_bracketed_text(input_string, expected):
    """
    Test removing text in brackets from string
    """
    assert dt.remove_bracketed_text(input_string) == expected


@pytest.mark.parametrize("url,expected", [
    ("http://yada.de", "yada.de"),
    ("www.fad.at", "www.fad.at"),
    ("https://diggr.link/blub/", "diggr.link/blub"),
    (None, None),
    ("", "")
])
def test_std_url(url, expected):
    """
    Test URL standardization function.
    """
    assert dt.std_url(url) == expected


@pytest.mark.parametrize("input_string, remove_strings, expected",[
    ("Evil Corp",None, "evil corp"),
    ("Evil Corp", ["corp"], "evil"),
    ("", ["abc"], ""),
    (None, None, None),
    ("Co. Ltd.", ["co ltd"], ""),
])
def test_std(input_string, remove_strings, expected):
    """
    Test string standarization function
    """
    assert dt.std(input_string, rm_strings=remove_strings) == expected