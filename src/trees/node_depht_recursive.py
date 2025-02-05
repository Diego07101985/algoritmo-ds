def nodeDepths(root, depht=0):
    if root is None:
        return 0

    return depht + nodeDepths(root.left, depht+1) + nodeDepths(root.right, depht+1) 
         
     


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
