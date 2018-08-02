import json
import string
import re
import os

PUNCT_TRANSTABLE = str.maketrans("","", string.punctuation)

def remove_html(s):
    """
    Removes html tags from string :s: .
    """
    if s:
        s = re.sub(r'<[^<]+?>', '', s)
        s = " ".join(s.split())
        s = s.strip()
    return s

def remove_punctuation(s):
    """
    Removes punctuation from string
    """
    if s:
        s = s.translate(PUNCT_TRANSTABLE)
    return s

def remove_bracketed_text(s):
    """
    Removes text in brackets from string :s: .
    """
    s = re.sub(r'\([^\()]+?\)', '', s)
    s = re.sub(r'\[[^\[]]+?\]', '', s)
    s = re.sub(r'\[[^\[]]+?\]', '', s)
    return s.strip()

def std_url(url):
    """
    Standardizes urls by removing protocoll and final slash.
    """
    if url:
        url = url.split("//")[-1]
        if url.endswith("/"):
            url = url[:len(url)-1]
    return url

def std(s, lower=True, rm_punct=True, rm_bracket=True, rm_spaces=False, rm_strings=None):
    """
    Combined string stardardization function.
    :lower:      lower case
    :rm_punct:   remove punctuation
    :rm_bracket: remove brackets () [] 
    :rm_spaces:  remove white spaces
    :rm_stirng:  list of substrings to be removed from string before comparison
    """
    if s:
        if lower:
            s = s.lower()
        
        if rm_punct:
            s = remove_punctuation(s)
        
        if rm_strings:
            for form in rm_strings:
                s = s.replace(form.lower(), "")
        
        if rm_bracket:
            s = remove_bracketed_text(s)

        if rm_spaces:
            s = s.replace(" ", "")

        s = s.strip()
    return s