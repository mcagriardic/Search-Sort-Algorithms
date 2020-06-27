### Bubble sort implementation ###
## O(N^2)

class BubbleSort:
    
    def __init__(self, lst):
        self.lst = lst
        
    def sort(self):
        for i in range(len(self.lst)):
            swap = False
            for j in range(len(self.lst) - 1):
                if self.lst[j] > self.lst[j + 1]:
                    swap = True
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]
            
            if not swap:
                print("Sorted list: %s" %self.lst)
                return 1

sort_instance = BubbleSort([3,1,5,6,2,7,5,6,3,5,9,5,55,2,4,8,9,6,2,20])
sort_instance.sort()