### Binary search implementation ###

# numpy is imported to generate lists
import numpy as np

class BinarySearch:
    
    def __init__(self, lst, val, verbose=False):
        self.lst = lst
        self.val = val
        self.verbose = verbose
        
        self.count = 0
        
        self.mid = None
        self.val_found = False
        self.stop_condition = False


    def set_mid(self):
        if len(self.lst) % 2 == 0:
            self.mid = int(len(self.lst) / 2 - 1)
            return 1
        self.mid = int(len(self.lst) / 2)
        return 1


    def remove_right(self):
        if self.verbose:
            print("Items removed...    %s" %self.lst[self.mid:])
            print("Items remaining...  %s\n" %self.lst[:self.mid])
        self.lst = self.lst[:self.mid]
        self.set_mid()

        
    def remove_left(self):
        if self.verbose:
            print("Items removed...    %s" %self.lst[:self.mid + 1])
            print("Items remaining...  %s\n" %self.lst[self.mid + 1:])
        self.lst = self.lst[self.mid + 1:]
        self.set_mid()

    
    def search(self):
        self.set_mid()
        while not self.val_found:
            if not self.lst:
                print("%s does not exist in %s" %(self.val, self.lst))
                return - 1
            if self.lst[self.mid] == self.val:
                print(
                    "Mid val %s is equal to value we are looking for %s..." 
                    %(self.lst[self.mid], self.val)
                )
                break
            elif self.lst[self.mid] > self.val:
                self.remove_right()
            elif self.lst[self.mid] < self.val:
                self.remove_left()

            self.count += 1

        print("\nTook %s steps..." %self.count)


generated_list = list(np.linspace(0, 2**25, num=2**25 + 1).astype(int))
search_instance = BinarySearch(\
    lst=generated_list,
    val=5,
    verbose=False)
search_instance.search()