### Selection sort implementation ###
## O(N^2) -> N x((N-1) + (N-2) + (N-3) + .... +1)

class SelectionSort:
    
    def __init__(self, lst):
        self.lst = lst
        self.initial_list = lst[:]
        
        self.lowest_index = None
        self.count = 0

    def sort(self):
        self.start_index = 0
        
        for val_index in range(self.start_index, len(self.lst)):
            self.lowest_index = self.start_index
            for inner_val_index in range(self.start_index + 1, len(self.lst)):
                if self.lst[inner_val_index] < self.lst[self.lowest_index]:
                    self.lowest_index = inner_val_index

                self.count += 1

            if self.lowest_index != val_index:
                self.lst[self.lowest_index], self.lst[self.start_index] = \
                self.lst[self.start_index], self.lst[self.lowest_index]

            self.start_index += 1
        
        print("Initial list:   %s..." %self.initial_list)
        print("Sorted list:    %s..." %self.lst)
        print("Took %s steps..." %self.count)

sort_instance = SelectionSort([3,1,5,6,2,7,5,6,3,5,9,5,55,2,4,8,9,6,2,20])
sort_instance.sort()