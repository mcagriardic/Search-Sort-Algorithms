def find_min_val(ro):
    
    if not ro:
        return None
    
    left = find_min_val(ro.l)
    
    if not left:
        return ro
    
    return left