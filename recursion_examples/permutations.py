def permutation(s):
    if len(s) == 1:
        return [s]

    perm_list = [] # resulting list
    for e in s:
        remaining_elements = [x for x in s if x != e]
        z = permutation(remaining_elements) # permutations of sublist
    
        for t in z:
            perm_list.append([e] + t)
    
    return perm_list

permutation("123")
# >> [['1', '2', '3'],
# >> ['1', '3', '2'],
# >> ['2', '1', '3'],
# >> ['2', '3', '1'],
# >> ['3', '1', '2'],
# >> ['3', '2', '1']]