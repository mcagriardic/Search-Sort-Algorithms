# Write a function that is passed an array of integers and a “target” number
# and that returns the number of occurrences of the target in the array.

def target_occurrence(l, t):

    if not l:
        return 0

    return (
        1 + target_occurrence(l[1:], t)
        if l[0] == t
        else target_occurrence(l[1:], t)
    )

target_occurrence([1,2,1,1,1], 1)

# >> 4

target_occurrence([1,2,1,1,1], 3)

# >> 0
