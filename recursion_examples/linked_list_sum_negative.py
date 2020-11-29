# Write a recursive function to compute the sum of just negative numbers in a linked list.

class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedList:

    def __init__(self, head):
        self.head = head


    def __sum_negative(self, head):

        if not head:
            return 0

        if head.val < 0:
            return head.val + self.__sum_negative(head.next_node)
        else:
            return self.__sum_negative(head.next_node)


    def sum_negative(self):
        return self.__sum_negative(self.head)


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

ll.sum_negative()

# >> -6
