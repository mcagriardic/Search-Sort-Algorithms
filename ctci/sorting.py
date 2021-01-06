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


def find_sub_section_to_sort(l):
    upper_idx = 0
    maxidx = 0
    to_sort = []
    for i in range(1, len(l)):
        if l[i] > l[maxidx]:
            maxidx = i
        elif l[i] < l[maxidx]:
            upper_idx = i
            to_sort.append(l[i])

    lower_number = min(to_sort)
    for i in range(len(l)):
        if l[i] > lower_number:
            lower_idx = i
            break

    return (lower_idx, upper_idx)

find_sub_section_to_sort([1,2,4,7,10,11,8,12,6,16,18,19])

"""
>> (3, 8)
"""

find_sub_section_to_sort([1, 2, 3, 7, 5, 6, 8, 9])

"""
>> (3, 5)
"""

find_sub_section_to_sort([1, 2, 3, 7, 5, 6, 8, 9, 1])

"""
>> (1, 8)
"""