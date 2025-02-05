# O(n) time | O(n) space
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
\


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return 
        
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums) 
    calculateBranchSums(node.right, newRunningSum, sums) 
    
    
    
    class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    stack = [{"root": root,  "sum": root.value}  ]
    sum_of_values = 0
    list = []
    while len(stack)>0:
        node = stack.pop()
       
        nodeInfo, sum = node['root'], node['sum']
        if nodeInfo is None:
            continue            

        #print(f"sum {sum} nodeInfo.right.value {nodeInfo.right.value if nodeInfo.right else nodeInfo.value}")
        if nodeInfo.left is None and nodeInfo.right is None:
            list.append(sum)
            
        stack.append({"root": nodeInfo.right,  "sum": sum+nodeInfo.right.value if nodeInfo.right else sum} )
        stack.append({"root": nodeInfo.left,  "sum": sum+nodeInfo.left.value if nodeInfo.left else sum})
    return list

