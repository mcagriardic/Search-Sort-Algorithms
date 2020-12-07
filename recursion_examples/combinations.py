def combination(cs, s):
    # cs -> character set
    # s -> sample
    if len(cs) == s:
        return [cs]
    
    # combs -> combinations
    combs = []
    # c -> character
    for c in cs:
        # e -> element
        # rc -> remaining characters
        rc = [e for e in cs if c != e]
        
        # cts -> combinations temp
        cst = combination(rc, s)
        
        # ct -> combination temp
        combs = combs + [ct for ct in cst if ct not in combs]
    
    return combs


combination([1,2,3,4], 3)
# >> [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]