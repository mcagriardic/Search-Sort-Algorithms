### Selection sort implementation ###
### With function, and with class ###
## O(N^2) -> N x((N-1) + (N-2) + (N-3) + .... +1) = N^2/2

class SelectionSort:
    
    def __init__(self, lst):
        self.lst = lst
        
    def sort(self):
        for start_idx in range(len(self.lst)):
            self.lowest_index = start_idx
            for inner_val_index in range(start_idx + 1, len(self.lst)):
                if self.lst[inner_val_index] < self.lst[self.lowest_index]:
                    self.lowest_index = inner_val_index

            if start_idx != self.lowest_index:
                self.lst[start_idx], self.lst[self.lowest_index] = \
                self.lst[self.lowest_index], self.lst[start_idx]


def selection_sort(lst):
    for start_idx in range(len(lst)):
        smallest_idx = start_idx
        for inner_idx in range(start_idx + 1, len(lst)):
            if lst[inner_idx] < lst[smallest_idx]:
                smallest_idx = inner_idx
        
        if start_idx != smallest_idx:
            lst[start_idx], lst[smallest_idx] = \
            lst[smallest_idx], lst[start_idx]
    
    return lst

sort_instance = SelectionSort([3,1,5,6,2,7,5,6,3,5,9,5,55,2,4,8,9,6,2,20])
sort_instance.sort()
print(sort_instance.lst)