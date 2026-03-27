"""String utility functions."""


def reverse(s):
    return s[::-1]


def capitalize_words(s):
    return s.title()


def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count


def truncate(s, length):
    """Truncate string to given length."""
    if len(s) <= length:
        return s
    return s[:length] + "..."
