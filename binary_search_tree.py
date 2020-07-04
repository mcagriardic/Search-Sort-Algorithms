class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):
    
    def __init__(self, root):
        self.root = root
        
    def search(self, val_to_search, root):
        if not root:
            print("Val does not exist!")
            return None
        
        if val_to_search > root.val:
            self.search(val_to_search, root.right)
        elif val_to_search < root.val:
            self.search(val_to_search, root.left)
        elif val_to_search == root.val:
            print("Val found!")
            return 1
        
    def insert(self, val_to_insert, root):
        if not root.right or not root.left:
            to_insert = TreeNode(val_to_insert)
            if val_to_insert > root.val:
                root.right = to_insert
            else:
                root.left = to_insert
            return 1
        
        if val_to_insert > root.val:
            self.insert(val_to_insert, root.right)
        elif val_to_insert < root.val:
            self.insert(val_to_insert, root.left)
            
    def delete(self, val_to_delete, root):
        if not root:
            return None
        
        if val_to_delete > root.val:
            root.right = self.delete(val_to_delete, root.right)
        elif val_to_delete < root.val:
            root.left = self.delete(val_to_delete, root.left)
        elif val_to_delete == root.val:
            
            if not root.right:
                return root.left
            
            if not root.left:
                return root.right
            
            if root.left and root.right:
                temp_var = root.right
                while temp_var.left:
                    temp_var = temp_var.left
                
                root.val = temp_var.val
                root.right = self.delete(temp_var.val, root.right)
            
        return root
            
    def traverse(
            self,
            root,
            inorder=True,
            postorder=False,
            preorder=False
        ):

        if not root:
            return None

        if preorder:
            print(root.val)
        self.traverse(root.left)
        if inorder:
            print(root.val)
        self.traverse(root.right)
        if postorder:
            print(root.val)