"""String utility functions."""


def reverse(s):
    return s[::-1]


def capitalize_words(s):
    result = ""
    words = s.split(" ")
    for i in range(len(words)):
        word = words[i]
        result = result + word[0].upper() + word[1:]
        if i < len(words) - 1:
            result = result + " "
    return result


def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count = count + 1
    return count


def truncate(s, length):
    """Truncate string to given length."""
    if len(s) <= length:
        return s
    result = ""
    for i in range(length):
        result = result + s[i]
    return result + "..."
