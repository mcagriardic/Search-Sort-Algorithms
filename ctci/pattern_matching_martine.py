import unittest


def count_number_of_pattern_occurances(pattern):
    """
    determine how many times a and b occurs in the given pattern
    :param pattern: a string of as and bs
    :return: number of as and bs, regardless of order stated in the pattern
    """
    first_count = 0
    second_count = 0
    
    if pattern[0] == 'a':
        first_count = pattern.count(pattern[0])
        second_count = pattern.count('b')
    elif pattern[0] == 'b':
        first_count = pattern.count(pattern[0])
        second_count = pattern.count('a')

    return first_count, second_count

def determine_first_value(first_count, value):
    """
    determine what the first pattern character is based on the pattern count
    :param first_count: how many times the first pattern character appeared
    :param value: string of characters
    :return: the combination of characters from value that the first character in the pattern is equal to.
    """
    first_pattern_as_value = ""
    for c, v in enumerate(value):
        if value.count(value[:c]) == first_count:
            first_pattern_as_value = value[:c]

    return first_pattern_as_value

def determine_second_value(second_count, value, first_pattern_as_value):
    """
    Determine based on the first character, what the second character combo should be.
    After stripping out all values equivalent to the first pattern character is,
    if the remaining values can't be divided as  a whole number by the number of the
    second pattern character, then there is no match and the function returns False
    :param second_count:
    :param value:
    :param first_pattern_as_value:
    :return:
    """

    temp_val = value.replace(first_pattern_as_value, "")
    if isinstance(len(temp_val)/second_count, float):
        return False
    else:
        second_pattern_as_value = temp_val[:len(temp_val) / second_count]
    return second_pattern_as_value

def pattern_matching(value, pattern):
    """
    After determining the pattern equivalents in the value string,
    check the mattern. By removing each translated character in the order of
    their appearance in the pattern, the remaining value should return empty if there
    is a match, else it will return False.
    :param value: string of characters
    :param pattern: string of a combination of a's and b's
    :return: True/False. If True then pattern match values, else False.
    """

    first_count, second_count = count_number_of_pattern_occurances(pattern)
    first_pattern_as_value = determine_first_value(first_count, value)

    second_pattern_as_value = determine_second_value(second_count, value, first_pattern_as_value)
    if second_pattern_as_value is False:
        return False

    for character in pattern:
        if character == pattern[0]:
            value = value.lstrip(first_pattern_as_value)
        else:
            value = value.lstrip(second_pattern_as_value)

    if len(value) == 0:
        return True
    else:
        return False


class UnitTest(unittest.TestCase):
    def test_pattern_match(self):
        self.assertTrue(pattern_matching('catcatcatgocatgogogogogocat', 'aaababbbbba'))

    def test_pattern_match_similar(self):
        self.assertTrue(pattern_matching('catcatcarcar', 'aabb'))

    def test_pattern_mismatch_similar(self):
        self.assertFalse(pattern_matching('catcatcacar', 'aabb'))

if __name__ == '__main__':
    unittest.main()