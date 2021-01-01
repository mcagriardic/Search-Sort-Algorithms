"""
Sort a linked list, 
Instead of creating a new list with sorted elements, 
edit the current list by inserting the unsorted value in it's sorted location, 
and remove the unsorted value from it's unsorted location. 
Eg
list 1 > 3 > 2 > 4 > 5
remove 3 from the 1 > X > 2 location
insert the value 3 into the 2 > X > 4 location. 
Todo: add a function which checks if the list is sorted, 
if not sorted, then run func traverse_list_for_sorting() again. 
"""

class Node:
    def __init__(self, v, n=None, p=None):
        # v -> value
        self.v = v
        # n -> next
        self.n = n
        # p -> previous
        self.p = p
        
class LinkedList:
    def __init__(self, h=None):
        # h -> head
        self.h = h
        
    def __insert(self,v):
        if not self.h:
            self.h = Node(v)
        else:
            # cn -> current node
            cn = self.h
            while cn:
                if not cn.n:
                    break
                cn = cn.n
            inserted = Node(v,n=None,p=cn)
            cn.n = inserted
            
    def insert(self, vs):
        # vs -> values
        if not isinstance(vs, list):
            vs = [vs]
        # v -> value
        [self.__insert(v) for v in vs]
        
    def __traverse(self, ro):
        # ro -> root
        if not ro:
            return None
        print(ro.v)
        self.__traverse(ro.n)
        
    def traverse(self):
        return self.__traverse(self.h)
    
    def get_elem_to_move(self):
        cn = self.h.n
        pn = cn.p
        while cn:
            if cn.v < cn.p.v:
                return cn ,pn
            pn = cn
            cn = cn.n
        return None, None

    def __sort(self, to_move):
        cn = self.h
        while cn:
            if cn.v > to_move.v:
                if cn == self.h:
                    to_move.n = self.h
                    to_move.p = None
                    self.h.p = to_move
                    self.h = to_move
                else:
                    to_move.n = cn
                    to_move.p = cn.p
                    cn.p.n = to_move
                    cn.p = to_move
                return None
            cn = cn.n

    def sort(self):
        cn = True
        while cn:
            # pn -> previous node
            cn, pn = self.get_elem_to_move()
            if not cn:
                # if there is not element to move
                # break the sorting loop
                break
            pn.n = cn.n
            # if the end node is the current node
            if cn.n:
                cn.n.p = pn
            self.__sort(cn)

ll = LinkedList()
ll.insert([1,6,3,2,4])
ll.sort()
ll.traverse()

"""
>> 1
>> 2
>> 3
>> 4
>> 6
"""

ll = LinkedList()
ll.insert([6,3,2,4])
ll.sort()
ll.traverse()

"""
>> 3
>> 2
>> 4
>> 6
"""