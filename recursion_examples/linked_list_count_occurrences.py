# Write a function that is passed a linked list of integers and a “target” number
# and that returns the number of occurrences of the target in the linked list.

class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedList:

    def __init__(self, head):
        self.head = head


    def __count_occurrences(self, head, target):

        if not head:
            return 0

        if head.val == target:
            return 1 + self.__count_occurrences(head.next_node, target)
        else:
            return self.__count_occurrences(head.next_node, target)


    def count_occurrences(self, target):
        return self.__count_occurrences(self.head, target)


minus_one = Node(-1)
minus_five = Node(-5)
four = Node(4)
eleven = Node(11)

minus_five.next_node = minus_one
minus_one.next_node = four
four.next_node = eleven

ll = LinkedList(minus_five)
ll.traverse()

# >> -5
# >> -1
# >> 4
# >> 11

print(ll.count_occurrences(1))
print(ll.count_occurrences(-1))

# >> 0
# >> 1
