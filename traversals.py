class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.value:

            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        elif key> self.value:

            if key <self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)



    def final(self):
        pass

    def preorder_traversal(self, root):
        if self.left:
            self.left.preorder_traversal(root)
        print(self.value)

        if self.right:
            self.right.preorder_traversal(root)

    def inorder_traversal(self, root):
        if self.left:
            self.left.inorder_traversal(root)

        print(self.value)

        def find(self, key):
            if key < self.value:
                if self.left is None:
                    return False
                else:
                    return self.left.find(key)
            elif key > self.value:
                if self.right is None:
                    return False
                else:
                    return self.right.find(key)
            else:
                return True

    def postorder_traversal(self, root):
        if self.left:
            self.left.postorder_traversal(root)

        if self.right:
            self.right.postorder_traversal(root)

        print(self.value)

if __name__ == "__main__":

    tree = TreeNode("p")

    tree.insert("11")
    tree.insert("12")
    tree.insert("13")
    tree.insert("14")
    tree.insert("14")
    tree.insert("15")
    tree.insert("16")
    tree.insert("17")
    tree.insert("18")
    tree.insert("19")
    tree.insert("20")


    print("\n Preorder Traversal")
    tree.preorder_traversal(tree)

    print("\n Inorder Traversal")
    tree.inorder_traversal(tree)

    print("\n Postorder Traversal")
    tree.postorder_traversal(tree)


