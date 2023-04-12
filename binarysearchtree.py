class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)

        if not self.root:
            self.root = new_node
            return

        curr_node = self.root
        while curr_node:
            if val < curr_node.val:
                if not curr_node.left:
                    curr_node.left = new_node
                    return
                else:
                    curr_node = curr_node.left
            else:
                if not curr_node.right:
                    curr_node.right = new_node
                    return
                else:
                    curr_node = curr_node.right

    def inorder_traversal(self, root):
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)



bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
print(bst.inorder_traversal(bst.root))  # Output: [1, 3, 5, 7, 9]
