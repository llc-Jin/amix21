from amix21 import greeting


def test_greeting_returns_hello_message():
    assert greeting("World") == "Hello, World!"


def test_greeting_strips_surrounding_whitespace():
    assert greeting("  Alice  ") == "Hello, Alice!"
