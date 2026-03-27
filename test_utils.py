from utils import reverse, capitalize_words, count_vowels, truncate


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("a") == "a"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_count_vowels():
    assert count_vowels("hello") == 2


def test_truncate():
    assert truncate("hello world", 5) == "hello..."
    assert truncate("hi", 5) == "hi"
    assert truncate("", 5) == ""
