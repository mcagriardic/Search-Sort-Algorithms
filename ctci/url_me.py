"""
from: Cracking the Coding Interview
Replace all spaces in a string with %20
"""
class UnitTest(unittest.TestCase):
    #url .replace solution
    def test_string_with_spaces(self):
        self.assertEqual(url_me("Hello, this is John"), "Hello,%20this%20is%20John")

    def test_string_no_spaces(self):
        self.assertEqual(url_me("Hello,thisisJohn"), "Hello,thisisJohn")

    def test_empty_str(self):
        self.assertEqual(url_me(""), "")

    #url alt solution tests below

    def test_string_with_spaces_alt_solution(self):
        self.assertEqual(url_me_alt_solution("Hello, this is John"), "Hello,%20this%20is%20John")

    def test_string_with_no_spaces_alt_solution(self):
        self.assertEqual(url_me_alt_solution("Hello,thisisJohn"), "Hello,thisisJohn")

    def test_empty_str_alt_solution(self):
        self.assertEqual(url_me_alt_solution(""), "")