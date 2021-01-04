"""
Hacker rank: https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
Given an integer, we need to find the super digit of the integer.
If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
For example, the super digit of 9875 will be calculated as:
    super_digit(9875)   9+8+7+5 = 29
    super_digit(29)     2 + 9 = 11
    super_digit(11)     1 + 1 = 2
    super_digit(2)      = 2
You are given two numbers n and k. The number p is created by concatenating
the string n k times. Continuing the above example where n = 9875, assume your value k = 4.
Your initial p = 9875987598759875.
Sample Input:
148 3
Sample Output:
4
"""

def super_digit(num, sumnum=0):
    sumnum += int(num[0])

    if len(num) == 1:
        if sumnum > 9 :
            return super_digit(str(sumnum), sumnum=0)
        else:
            return sumnum
    return super_digit(num[1:], sumnum=sumnum)

super_digit("9875")

"""
>> 2
"""

super_digit("148")

"""
>> 4
"""