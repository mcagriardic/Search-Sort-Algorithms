"""
From: Cracking the Coding Interview
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string.
"""

class UnitTest(unittest.TestCase):
    def test_string_compression(self):
        self.assertEqual(compress_me("aaaabbbccddaa"), "a4b3c2d2a2")

    def test_string_comp_s_shorter_then_comp(self):
        self.assertEqual(compress_me("abcde"), "abcde")

    def test_empty_string(self):
        self.assertEqual(compress_me(""), -1)