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
Complexity of comparison: O(n^2)

TOTAL: O(n*logn) + O(n^2)
TOTAL: O(n^2)
"""

def smallest_dif(n1s, n2s):
    n1s.sort()
    n2s.sort()

    diff = None
    for n1 in n1s:
        for n2 in n2s:
            print(n1,n2)
            if n1 < n2:
                if not diff or abs(n1 - n2) < diff:
                    diff = abs(n1 - n2)
                break
            else:
                if not diff or abs(n1 - n2) < diff:
                    diff = abs(n1 - n2)

    return diff

ns1 = [1, 3, 15, 11, 2]
ns2 = [23, 127, 235, 19, 8]

smallest_dif(ns1, ns2)

"""
>> 3
"""