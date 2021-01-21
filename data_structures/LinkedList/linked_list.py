class Node:
    def __init__(self, node, next_node=None):
        self.node = node
        self.next_node = next_node


class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def print_elements(self):
        current_node = self.first_node
        print(self.first_node.node)

        while current_node.next_node != None:
            current_node = current_node.next_node
            print(current_node.node)
            
    def search(self, val):
        current_node = self.first_node
        index = 0
        
        while True and current_node:
            if current_node.node == val:
                print("Val found at index %s..." %index)
                return 1
            current_node = current_node.next_node
            index += 1

        print("Val not found...")

    def read(self, index):
        current_node = self.first_node
        starting_index = 0
        
        while starting_index < index:
            current_node = current_node.next_node
            starting_index += 1
        
        if current_node:
            print(current_node.node)
        else:
            print("Index out of range...")

    def insert(self, index, val):
        new_node = Node(val)
        if index == 0:
            temp_node_holder = self.first_node
            self.first_node = new_node
            self.first_node.next_node = temp_node_holder
        else:
            current_node = self.first_node
            starting_index = 0
            while starting_index < index - 1:
                current_node = current_node.next_node
                starting_index += 1 
                
            temp_node_holder = current_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
            
    def delete(self, index):
        if index == 0:
            self.first_node = self.first_node.next_node
        else:
            current_node = self.first_node
            starting_index = 0
            while starting_index < index:
                if starting_index == index - 1:
                    node_before_deleted_node = current_node
                current_node = current_node.next_node
                starting_index += 1 
                
            node_before_deleted_node.next_node = current_node.next_node

node_1 = Node(8)

node_2 = Node(9)
node_1.next_node = node_2

node_3 = Node(10)
node_2.next_node = node_3

linked_list = LinkedList(node_1)

### Some operations on linked lists ###
linked_list.insert(1,5)
linked_list.delete(3)
linked_list.search(9)
linked_list.read(2)
linked_list.print_elements()