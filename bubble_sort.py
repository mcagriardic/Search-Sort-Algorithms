### Bubble sort implementation ###
### With function, and with class ###
## O(N^2)

class BubbleSort:
    
    def __init__(self, lst):
        self.lst = lst
        
        self.count = 0
        
    def sort(self):
        for i in range(len(self.lst)):
            swap = False
            for j in range(len(self.lst) - 1):
                if self.lst[j] > self.lst[j + 1]:
                    swap = True
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]
            
            if not swap:
                break


def bubble_sort(lst_to_sort):
    for i in range(len(lst_to_sort)):
        swap = False
        for j in range(len(lst_to_sort) - 1):
            if lst_to_sort[j] > lst_to_sort[j + 1]:
                swap = True
                lst_to_sort[j], lst_to_sort[j + 1] = \
                lst_to_sort[j + 1], lst_to_sort[j]
            
        if not swap:
            break
    
    return lst_to_sort


sort_instance = BubbleSort([3,1,5,6,2,7,5,6,3,5,9,5,55,2,4,8,9,6,2,20])
sort_instance.sort()
print(sort_instance.lst)