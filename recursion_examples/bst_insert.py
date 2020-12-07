# Write a recursive function that is passed a binary search tree’s root pointer and
# a new value to be inserted and that creates a new node with the new value,
# placing it in the correct location to maintain the binary search tree
# structure.Hint: Consider making the root pointer parameter a reference parameter.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def traverse(self, root):
        if not root:
            return None
        self.traverse(root.left)
        print(root.val)
        self.traverse(root.right)

    def insert(self, root, val):

        if not root.right or not root.left:
            if root.val > val:
                root.left = TreeNode(val)
            else:
                root.right = TreeNode(val)
            return None

        if root.val < val:
            return self.insert(root.right, val)

        if root.val >= val:
            return self.insert(root.left, val)

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
#      4+  11   30  40    52  61  82  95

##

bst.traverse(root)

# >> 4
# >> 10
# >> 11
# >> 25
# >> 30
# >> 33
# >> 40
# >> 50
# >> 52
# >> 56
# >> 61
# >> 75
# >> 82
# >> 89
# >> 95

bst.insert(root, 31)

bst.traverse(root)

# >> 4
# >> 10
# >> 11
# >> 25
# >> 30
# >> 31
# >> 33
# >> 40
# >> 50
# >> 52
# >> 56
# >> 61
# >> 75
# >> 82
# >> 89
# >> 95
