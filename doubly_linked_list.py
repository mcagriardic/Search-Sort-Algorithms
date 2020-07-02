### Doubly Linked List and Queue implementation ###

class NodeDL(object):
    
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node


class DoublyLinkedList(object):
    
    def __init__(self, first_node, last_node):
        self.first_node = first_node
        self.last_node = last_node
        
    def print_elements(self, fw=True):
        if fw:
            current_node = self.first_node
            print(self.first_node.val)
        
            while current_node.next_node != None:
                current_node = current_node.next_node
                print(current_node.val)

        elif not fw:
            current_node = self.last_node
            print(self.last_node.val)
            
            while current_node.prev_node != None:
                current_node = current_node.prev_node
                print(current_node.val)
                
    def insert_at_end(self, val):
        node_to_insert = NodeDL(val,self.last_node)
        self.last_node.next_node = node_to_insert
        self.last_node = node_to_insert

    def remove_from_beg(self):
        new_first_node = self.first_node.next_node
        new_first_node.prev_node = None
        self.first_node = new_first_node
        

class Queue(object):
    
    def __init__(self, DLList_instance):
        self.queue = DLList_instance
        
    def enque(self, val):
        self.queue.insert_at_end(val)
    
    def deque(self):
        self.queue.remove_from_beg()
        
    def tail(self):
        self.queue.last_node


### to test ###

## initiate DoublyLinkedList
node_1 = NodeDL(1)
node_2 = NodeDL(2)
node_3 = NodeDL(3)

node_1.next_node = node_2

node_2.prev_node = node_1
node_2.next_node = node_3

node_3.prev_node = node_2

dlinked_list = DoublyLinkedList(node_1, node_3)

## initiate Queue

queue = Queue(dlinked_list)

## test DoublyLinkedList methods

#insertion
dlinked_list.insert_at_end(5)
dlinked_list.print_elements(fw=False)

#removal
dlinked_list.remove_from_beg()
dlinked_list.print_elements(fw=False)

## test Queue methods

# Add to the queue
queue.enque(15)
queue.queue.print_elements()

# Remove from the queue
queue.deque()
queue.queue.print_elements()