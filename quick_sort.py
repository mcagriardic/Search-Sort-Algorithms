### Quick sort implementation ###
## O(N^2) -> Worst case, O(nlog(n)) -> Average case

def partition(lst, lp_idx, rp_idx):
    pivot = rp_idx
    rp_idx -= 1
    
    while True:
        while lst[lp_idx] < lst[pivot]:
            lp_idx += 1
        while lst[rp_idx] > lst[pivot]:
            rp_idx += -1
            
        if lp_idx >= rp_idx:
            lst[lp_idx], lst[pivot] = \
            lst[pivot], lst[lp_idx]
            break
        else:
            lst[lp_idx], lst[rp_idx] = \
            lst[rp_idx], lst[lp_idx]
    return lp_idx

def quick_sort(lst, lp_idx, rp_idx):
    if lp_idx >= rp_idx:
        return lst
    
    pivot = partition(lst, lp_idx, rp_idx)
    quick_sort(lst, lp_idx, pivot - 1)
    quick_sort(lst, pivot + 1, rp_idx)
    
    return lst