from input import understand_input
from search_web import build_url
import pytest

"""
This is where we test our two functions and their edge cases
"""


def test_understand_input_open():
    assert understand_input("open calculator") == ("open", "calculator")
    assert understand_input("open file") == ("open", "file")


def test_understand_input_search():
    assert understand_input("search youtube") == ("search", "youtube")
    assert understand_input("search google") == ("search", "google")


def test_understand_input_invalid():
    assert understand_input("hello there") == ("invalid", None)
    assert understand_input("bye bye") == ("invalid", None)


def test_understand_input_ask():
    assert understand_input("ask something") == ("ask", "something")
    assert understand_input("ask what is gravity") == ("ask", "what is gravity")


def test_understand_input_joke():
    assert understand_input("joke") == ("joke", None)


def test_understand_input_quit():
    assert understand_input("exit") == ("invalid", None)
    with pytest.raises(SystemExit):
        assert understand_input("quit")


def test_build_url():
    assert build_url("youtube") == "https://www.google.com/search?q=youtube"
    assert build_url("black holes") == "https://www.google.com/search?q=black+holes"
