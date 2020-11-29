# Write a recursive function that is given a singly linked list where the data
# type is integer returns the count of negative numbers in the list


class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class LinkedList:

    def __init__(self, head):
        self.head = head


    def __traverse(self, head):
        if not head:
            return None

        print(head.val)
        return self.__traverse(head.next_node)


    def __traverse_bw(self, head):
        if not head:
            return None

        self.__traverse_bw(head.next_node)
        print(head.val)
        return None


    def __count_negative(self, head):
        if not head:
            return 0

        list_count = self.__count_negative(head.next_node)

        if head.val < 0:
            list_count += 1
        return list_count


    def traverse(self):
        return self.__traverse(self.head)


    def traver_bw(self):
        return self.__traverse_bw(self.head)


    def count_negative(self):
        return self.__count_negative(self.head)


minus_one = Node(-1)
eleven = Node(11)

minus_five = Node(-5, minus_one)

four = Node(4, eleven)
minus_one.next_node = four


ll = LinkedList(minus_five)

ll.traverse()

# >> -5
# >> -1
# >> 4
# >> 11

ll.count_negative()

# >> 2
