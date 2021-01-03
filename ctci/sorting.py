"""
Cracking the Coding Interview
Given an array of integers, write a method to find indices m and n
such that if you sorted elements m through n the entire array would be sorted.
"""

class UnitTest(unittest.TestCase):
    def test_original_test_case(self):
        self.assertEqual(find_sub_section_to_sort([1,2,4,7,10,11,8,12,6,16,18,19]), (3, 8))

    def test_simple_test_case(self):
        self.assertEqual(find_sub_section_to_sort([1, 2, 3, 7, 5, 6, 8, 9]), (3, 5))

    def test_entire_list_test_case(self):
        self.assertEqual(find_sub_section_to_sort([1, 2, 3, 7, 5, 6, 8, 9, 1]), (0, 8))