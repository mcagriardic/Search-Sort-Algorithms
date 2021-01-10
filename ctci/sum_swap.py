"""
Cracking the Coding Interview
Sum Swap
Given two arrays of integers, find a pair of values (
one value from each array) that you can swap to
give the two arrays the same sum.
Example:
    input: [4, 1, 2, 1, 1, 2]
            [3, 6, 3, 3]
    output: [1, 3]
"""

def get_sum_and_unique_elems(ns):
    sum_ = 0
    set_ = set()
    for n in ns:
        sum_ += n
        set_.add(n)
    return sum_, set_

def sum_swap(ns1, ns2):
    sum1, set1 = get_sum_and_unique_elems(ns1)
    sum2, set2 = get_sum_and_unique_elems(ns2)
    equal_sum = (sum1 + sum2) / 2

    for n1 in set1:
        if equal_sum - (sum1 - n1) in set2:
            yield n1, int(equal_sum - (sum1 - n1))

list(sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))

"""
>> [(1, 3), (4, 6)]
"""