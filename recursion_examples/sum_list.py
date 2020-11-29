# Sum of a list.

# INCORRECT IMPLEMENTATION; unnecessary paramater-agg.
def sum_list(l, agg=0):
    if not l:
        return agg

    agg += l[0]
    return sum_list(l[1:], agg=agg)

# CORRECT IMPLEMENTATION
def sum_list2(l):
    if not l:
        return 0

    return l[0] + sum_list(l[1:])

sum_list([1,2,3,45])
sum_list2([1,2,3,45])

# >> 51
# >> 51
