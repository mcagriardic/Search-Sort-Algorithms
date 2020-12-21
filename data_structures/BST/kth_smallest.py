# find the kth smallest element in a BST

k = 0

def find_kth_smallest(ro, kt):
    global k
    k = kt
    return __find_kth_smallest(ro)

def __find_kth_smallest(ro):
    global k
    if not ro:
        return None
    
    l = __find_kth_smallest(ro.l)
    
    if l:
        return l
    
    k -= 1
    if k == 0:
        return ro
    
    return __find_kth_smallest(ro.r)
    
