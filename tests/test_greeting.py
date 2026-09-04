import pytest

from amix21 import greeting


def test_greeting_returns_hello_message():
    assert greeting("World") == "Hello, World!"


def test_greeting_strips_surrounding_whitespace():
    assert greeting("  Alice  ") == "Hello, Alice!"


def test_greeting_rejects_empty_name():
    with pytest.raises(ValueError):
        greeting("")


def test_greeting_rejects_whitespace_only_name():
    with pytest.raises(ValueError):
        greeting("   ")
