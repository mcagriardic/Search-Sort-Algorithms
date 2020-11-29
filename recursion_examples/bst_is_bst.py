# A binary search tree is a binary tree in which each node value is greater than
# any value in that node’s left subtree but less than any value in the node’s
# right subtree. Write a recursive function to determine whether a binary tree
# is a binary search tree.


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


    def is_bst(self, root):
        """
            The logic here is; grab the root of the bst; is the root's val
            greater than the value to its immediate left and less than the
            value to its immediate right? If true, the binary tree assumpt
            ion is not violated for this node; move to next node. Change t
            he active node to left, and to right; repeat the process.
        """

        if not root:
            return True

        if root.left and root.val < root.left.val:
            print("Active root value: %s , its left node value: %s " %(root.val, root.left.val))
            print("Left node val is greater than the root val...")
            print("BST assumption is violated.")
            return False

        if root.right and root.val > root.right.val:
            print("Active root alue: %s , Its right node value: %s " %(root.val, root.right.val))
            print("Right node val is less than the root val...")
            print("BST assumption is violated.")
            return False

        return self.is_bst(root.left) and self.is_bst(root.right)

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
right_1_right_right = TreeNode(88)

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
#      4  11   30  40    52  61  82  88

##

bst.is_bst(root)

# >> Active root alue: 89 , Its right node value: 88
# >> Right node val is less than the root val...
# >> BST assumption is violated.
