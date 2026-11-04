"""Simple character, word, and line counts for strings."""


def _check_text(text):
    if not isinstance(text, str):
        raise TypeError("text must be an instance of str")


def count_characters(text):
    """Return the number of characters, including spaces and newlines."""
    _check_text(text)
    return len(text)


def count_words(text):
    """Return the number of words separated by any whitespace."""
    _check_text(text)
    return len(text.split())


def count_lines(text):
    """Return the splitlines count, with zero lines for an empty string."""
    _check_text(text)
    return len(text.splitlines())
