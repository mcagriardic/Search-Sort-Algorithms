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
Complexity of comparison: O(ns2+ns1-1)
Complexity of comparison: O(ns2+ns1)
Complexity of comparison: O(n)

TOTAL: O(n*logn) + O(n)
TOTAL: O(n*logn)
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

            if abs(n1 - n2) > diff:
                break

    return diff

ns1 = [1, 3, 15, 11, 2]
ns2 = [23, 127, 235, 19, 8]

smallest_dif(ns1, ns2)

"""
>> 3
"""

# worst case:

ns1 = [17,18,19,20,21]
ns2 = [1,2,3,4,5]

smallest_dif(ns1, ns2)

# comparisons:

"""
17 1
17 2
17 3
17 4
17 5
18 1
19 1
20 1
21 1
"""

"""
>> 12
"""
