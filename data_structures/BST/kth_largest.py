# Find the kth largest element in a BST

c = 0

def find_kth_largest(ro, k):
    global c
    if not ro:
        return None
    
    r = find_kth_largest(ro.r, k)
    c += 1
    if r:
        return r
            
    if c == k:
        return ro
    
    return find_kth_largest(ro.l, k)
