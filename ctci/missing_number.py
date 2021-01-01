# https://github.com/thundergolfer/interview-with-python/tree/master/problems/missing-number

"""
Missing Number
Write a function that accepts an array of integers in random order of
unknown length, but with one number missing. Return the missing number.
"""

def get_missing_number(ns):
    # maxn -> max number
    maxn = float('-inf')

    # suml -> sum list
    suml = 0
    for n in ns:
        if n > maxn:
            maxn = n
        suml += n

    return (maxn * (maxn + 1)) / 2 - sum

# tcs -> test cases
tcs = [
    [1,5,3,6,4,2,8,9,10],
    [1,5,4,3]
]
answers = [7, 2]
print([get_missing_number(t) == a for t,a in zip(tcs, answers)])

"""
>> [True, True]
"""
