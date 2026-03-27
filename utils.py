"""String utility functions."""


def reverse(s):
    return s[::-1]


def capitalize_words(s):
    return s.title()


def count_vowels(s):
    return sum(1 for c in s if c in "aeiouAEIOU")


def truncate(s, length):
    """Truncate string to given length."""
    if len(s) <= length:
        return s
    return s[:length] + "..."
