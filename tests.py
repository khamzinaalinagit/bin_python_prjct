import unittest
import tempfile
import os

from funcs import (
    is_binary_string,
    find_binaries_in_text,
    find_binaries_in_file,
)


class TestBinaryUtils(unittest.TestCase):
    def test_is_binary_string_valid(self):
        self.assertTrue(is_binary_string("0"))
        self.assertTrue(is_binary_string("1"))
        self.assertTrue(is_binary_string("1010"))
        self.assertTrue(is_binary_string("000111"))
        self.assertTrue(is_binary_string("   1011   "))

    def test_is_binary_string_invalid(self):
        self.assertFalse(is_binary_string(""))
        self.assertFalse(is_binary_string("2"))
        self.assertFalse(is_binary_string("10201"))
        self.assertFalse(is_binary_string("abc"))
        self.assertFalse(is_binary_string("10 10"))

    def test_find_binaries_in_text_basic(self):
        text = "values: 1010, 102, 000111, hello, 1110001."
        result = find_binaries_in_text(text)
        self.assertEqual(result, ["1010", "000111", "1110001"])

    def test_find_binaries_in_text_empty(self):
        text = "no binaries here"
        result = find_binaries_in_text(text)
        self.assertEqual(result, [])

    def test_find_binaries_in_file(self):

        content = "a 101 b 222 c 1110"
        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        try:
            result = find_binaries_in_file(tmp_path)
            self.assertEqual(result, ["101", "1110"])
        finally:
            os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
