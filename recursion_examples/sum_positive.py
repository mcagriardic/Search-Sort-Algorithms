# Write a recursive function to compute the sum of just positive numbers in
# an array.

def sum_positive(l):

    if not l:
        return 0

    return (
        l[0] + sum_positive(l[1:])
        if l[0] > 0
        else sum_positive(l[1:])
    )

sum_positive([1,2,3,-4])

# >> 6
