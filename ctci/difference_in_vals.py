"""
Cracking the Coding Interview

Given two arrays of numbers, calculate the pair
with the smallest difference between them. Eg:

ns1 = [1, 3, 15, 11, 2]
ns2 = [23, 127, 235, 19, 8]

Answer = 11,8 (diff = 3)
"""

"""
Initial complexity of sorting: O(n*logn)
Complexity of comparison: O(n1s + n2s)
Complexity of comparison: O(n)

TOTAL: O(n*logn) + O(n)
TOTAL: O(n*logn)
"""

def smallest_dif(n1s, n2s):
    n1s.sort()
    n2s.sort()

    idx1 = 0
    idx2 = 0
    diff = float('inf')
    while idx1 < len(n1s) and idx2 < len(n2s):
        tdiff = abs(n1s[idx1] - n2s[idx2])
        diff = min(tdiff, diff)

        if n1s[idx1] < n2s[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    return diff

ns1 = [1, 3, 15, 11, 2]
ns2 = [23, 127, 235, 19, 8]

smallest_dif(ns1, ns2)

"""
>> 3
"""