"""
hackerrank: https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
Davis has a number of staircases in his house and he likes to climb each staircase 1, 2
or 3 steps at a time. Being a very precocious child,
he wonders how many ways there are to reach the top of the staircase.
Given the respective heights for each of the  staircases in his house,
find and print the number of ways he can climb each staircase,
module 10^9 + 7 on a new line.
For example, there is s = 1 staircase in the house that is n = 5 steps high.
There are 13 possible ways he can take these 5 steps.
Sample input:
3
1
3
7
Sample Output:
1
4
44
"""

import timeit

# Without dynamic programming
# nodp -> no dymanic programming
def calculate_permutations_nodp(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4

    return (
        calculate_permutations_nodp(n - 1) + 
        calculate_permutations_nodp(n - 2) + 
        calculate_permutations_nodp(n - 3)
    )

%timeit for x in range(50): calculate_permutations_nodp(25)

"""
>> "6.86 s ± 4.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)"
"""

# With dynamic programming
def __calculate_permutations(n, cache):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4

    if n in cache:
        return cache[n]

    cache[n] = (
        __calculate_permutations(n - 1, cache) +
        __calculate_permutations(n - 2, cache) +
        __calculate_permutations(n - 3, cache)
        )

    return cache[n]

# dp -> dynamic programming
def calculate_permutations_dp(n):
    return __calculate_permutations(n, {})

%timeit for x in range(50): calculate_permutations_dp(25)

"""
513 µs ± 657 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
"""