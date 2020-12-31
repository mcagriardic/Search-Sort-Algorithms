"""
Cracking to Coding Interview
You are given list of integers both positive and negative.
Find the continuous sequence with the largest sum.

Eg Input: [2, -8, 3, -2, 4, -10]
Output: 5 (because of 3, -2, 4)
"""

i1 = [2, -8, 3, -2, 4, -10]
i2 = [7, -9, 2, 3, -3, 2, -10]

def greatest_cont_sum(input):
    sum = 0
    tsum = 0
    for n in input:
        tsum += n
        if tsum > sum:
            sum = tsum
        elif tsum < 0:
            tsum = 0

    return sum

for tc in [i1, i2]:
    print(greatest_cont_sum(tc))

"""
>> 5
>> 7
"""