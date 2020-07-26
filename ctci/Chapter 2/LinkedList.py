from random import randint

class LinkedListNode(object):
    
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node
        
    def __str__(self):
        return str(self.val)


class LinkedList(object):
    
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)
            
    def __str__(self):
        values = [str(node.val) for node in self]
        return "-> ".join(values)
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next_node
            
    def __len__(self):
        for len_, val in enumerate(self):
            continue
        return len_ + 1
            
    def add(self, val):
        if not self.head:
            self.head = self.tail = LinkedListNode(val)
        else:
            self.tail.next_node = LinkedListNode(val)
            self.tail = self.tail.next_node
    
    def add_multiple(self, values):
        for val in values:
            self.add(val)
            
    def generate(self, n, min_, max_):
        for count in range(n):
            self.add(randint(min_, max_))