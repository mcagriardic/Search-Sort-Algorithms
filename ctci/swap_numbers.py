"""
Cracking the Coding Interview
Swap the values of two variables, in place (without the use of a temp variable)
"""

class UnitTest(unittest.TestCase):
    def test_number_swap(self):
        self.assertEqual(swap_nums(150, 20), (20, 150))

    def test_large_number_swap(self):
        self.assertEqual(swap_nums(15023465362353456346, 1353416527268657), (1353416527268657, 15023465362353456346))

    def test_neg_number(self):
        self.assertEqual(swap_nums(-3, -1), (-1, -3))
