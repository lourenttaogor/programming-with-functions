"""
Writing a pytest code for the given code.
"""

from week2.passwords import word_in_file
import pytest

def test_word_in_file():
    # Test with a common password
    assert word_in_file("password123", "toppasswords.txt", True) == True
    # Test with a dictionary word
    assert word_in_file("hello", "wordlist.txt", False) == True
    # Test with a non-existent word
    assert word_in_file("nonexistentword", "toppasswords.txt", True) == False
    # Test with an empty string
    assert word_in_file("", "toppasswords.txt", True) == False

test_word_in_file()
