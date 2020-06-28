### Insertion sort implementation ###
### With function, and with class ###

class InsertionSort:
    
    def __init__(self, lst):
        self.lst = lst
        
    def sort(self):
        for i in range(1, len(self.lst)):
            while i > 0 and self.lst[i] < self.lst[i-1]:
                self.lst[i-1] , self.lst[i] = self.lst[i], self.lst[i-1]
                i -= 1

def insertion_sort(lst):
    for temp_index in range(1, len(lst)):
        
        while temp_index > 0 and lst[temp_index] < lst[temp_index - 1]:
            lst[temp_index], lst[temp_index - 1] = \
            lst[temp_index - 1], lst[temp_index]
            
            temp_index -= 1
            
    return lst

sort_instance = InsertionSort([3,1,5,6,2,7,5,6,3,5,9,5,55,2,4,8,9,6,2,20])
sort_instance.sort()
print(sort_instance.lst)