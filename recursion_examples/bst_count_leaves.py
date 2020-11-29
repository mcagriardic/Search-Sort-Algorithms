# For a class that implements a binary tree, add a publicly accessible method
# that returns the number of leaves (nodes without children) in the tree. The
# counting of leaves should be performed using recursion.


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):

    def __init__(self, root):
        self.root = root


    def __count_leaves(self, root):

        if not root:
            return 0

        if (not root.left) & (not root.right):
            return 1

        count = self.__count_leaves(root.left)
        count += self.__count_leaves(root.right)

        return count


    def count_leaves(self):
        return self.__count_leaves(self.root)


left_1 = TreeNode(25)
right_1 = TreeNode(75)

left_1_left = TreeNode(10)
left_1_right = TreeNode(33)

left_1_left_left = TreeNode(4)
left_1_left_right = TreeNode(11)

left_1_right_left = TreeNode(30)
left_1_right_right = TreeNode(40)

right_1_left = TreeNode(56)
right_1_right = TreeNode(89)

right_1_left_left = TreeNode(52)
right_1_left_right = TreeNode(61)

right_1_right_left = TreeNode(82)
right_1_right_right = TreeNode(95)

root = TreeNode(50, left_1, right_1)

left_1.left = left_1_left
left_1.right = left_1_right

left_1_left.left = left_1_left_left
left_1_left.right = left_1_left_right

left_1_right.left = left_1_right_left
left_1.right.right = left_1_right_right


right_1.left = right_1_left
right_1.right = right_1_right

right_1_left.left = right_1_left_left
right_1_left.right = right_1_left_right

right_1_right.left = right_1_right_left
right_1_right.right = right_1_right_right

bst = BinarySearchTree(root)

### EXAMPLE ###
## Construct the tree

#                     50
#             /                \
#            25                75
#         /      \          /      \
#        10      33        56      89
#       / \     /  \      /  \    /  \
#      4  11   30  40    52  61  82  95

##

bst.count_leaves()

# >> 8
