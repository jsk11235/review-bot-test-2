from utils import reverse, capitalize_words, count_vowels


def test_reverse():
    assert reverse("hello") == "olleh"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_count_vowels():
    assert count_vowels("hello") == 2
