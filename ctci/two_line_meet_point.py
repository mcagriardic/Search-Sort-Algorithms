"""
Cracking the Coding Interview
Given two straight lines write a function which determines when they meet.
The lines are represented on a x, y grid. y and x is provided for each line.
Example:
    4|_|X|_|_|
    3|O|O|O|O|
    2|_|X|_|_|
    1|_|X|_|_|
     1 2 3  4
X = x_axis = (start: 2, end: 2)
    y_axis = (start: 1, end: 4)
    data_s = [[2,2], [1, 4]]
O = x_axis = (start: 1, end: 4)
    y_axis = (start: 3, end: 3)
    data_s = [[1,4], [3, 3]]
"""

class UnitTest(unittest.TestCase):
    def test_array_overlaps(self):
        self.assertEqual(two_line_overlap([[2, 2], [1, 4]], [[1, 4], [3, 3]]), [2, 3])

    def test_array_overlaps_two(self):
        self.assertEqual(two_line_overlap([[1, 4], [1, 4]], [[1, 4], [1, 4]]), [1, 1])

    def test_no_overlap(self):
        self.assertEqual(two_line_overlap([[9, 13], [10, 10]], [[1, 4], [1, 4]]), -1)