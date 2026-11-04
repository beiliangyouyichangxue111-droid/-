"""Tests for string statistics."""

import unittest

from utils.text_stats import count_characters, count_lines, count_words


class TextStatsTests(unittest.TestCase):
    def assert_counts(self, text, characters, words, lines):
        self.assertEqual(count_characters(text), characters)
        self.assertEqual(count_words(text), words)
        self.assertEqual(count_lines(text), lines)

    def test_empty_string(self):
        self.assert_counts("", 0, 0, 0)

    def test_english_text(self):
        self.assert_counts("Hello, world!", 13, 2, 1)

    def test_chinese_text(self):
        self.assert_counts("你好，世界", 5, 1, 1)

    def test_mixed_chinese_and_english(self):
        self.assert_counts("你好 world 世界", 11, 3, 1)

    def test_spaces_and_tabs(self):
        self.assert_counts(" a\t b  ", 7, 2, 1)

    def test_unicode_whitespace(self):
        self.assert_counts("你好\u3000world", 8, 2, 1)

    def test_whitespace_only(self):
        for text, characters, lines in [
            ("   ", 3, 1),
            ("\t\u3000", 2, 1),
            ("\t\r\n\u3000", 4, 2),
            ("\n\n", 2, 2),
        ]:
            with self.subTest(text=text):
                self.assert_counts(text, characters, 0, lines)

    def test_single_and_multiple_lines(self):
        self.assert_counts("abc", 3, 1, 1)
        self.assert_counts("a\nb\nc", 5, 3, 3)

    def test_trailing_newlines(self):
        self.assert_counts("a\n", 2, 1, 1)
        self.assert_counts("a\n\n", 3, 1, 2)

    def test_crlf_is_one_line_break(self):
        self.assert_counts("a\r\nb", 4, 2, 2)
        self.assert_counts("a\r\n", 3, 1, 1)

    def test_non_string_inputs(self):
        for function in (count_characters, count_words, count_lines):
            for value in (None, 123, 1.5, True, b"bytes", ["a"]):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaisesRegex(TypeError, "text.*str"):
                        function(value)

    def test_str_subclasses_are_accepted(self):
        class CustomString(str):
            pass

        self.assert_counts(CustomString("a b\n"), 4, 2, 1)


if __name__ == "__main__":
    unittest.main()
