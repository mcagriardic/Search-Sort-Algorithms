# ALGO EXPLAINED
# stack excutes the last call. Last call to first:

# LAST CALL = L
# l = [[]]
# l + [[3] + e for e in l]
# >> [[], [3]]

# L - 1
# l = [[], [3]]
# l + [[2] + e for e in l]
# >> [[], [3], [2], [2, 3]]

# L - 2
# l = [[], [2], [3], [2,3]]
# l + [[1] + e for e in l]
# >> [[], [2], [3], [2, 3], [1], [1, 2], [1, 3], [1, 2, 3]]

# In total 3 calls are made which is len(cs)

def all_subsets(cs):
    
    if len(cs) == 0:
        return [[]]
    
    z = all_subsets(cs[1:])
    
    return z + [[cs[0]] + e for e in z]


all_subsets([1,2,3])
# >> [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]