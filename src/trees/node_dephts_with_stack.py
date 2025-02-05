def nodeDepths(root):
    # Write your code he
    sumOfDephts = 0
    stack = [{"node":root, "depth":0}]
    while len(stack) > 0 :
        nodeInfo =  stack.pop()
        node, depth = nodeInfo['node'], nodeInfo['depth']
        print("remove stack")
        print(f"BinaryTree(value={ node.value if node else 'Nan'})")
        if node is None:
            continue
        sumOfDephts += depth
        stack.append({"node":node.left,  "depth":depth+1})
        stack.append({"node":node.right,  "depth":depth+1})

        print("put in stack")
        print(f"BinaryTree(value={ node.left.value if node.left else 'Nan'})")
        print(f"BinaryTree(value={node.right.value if node.right else 'Nan'})")

    return sumOfDephts


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"BinaryTree(value={self.value})"
