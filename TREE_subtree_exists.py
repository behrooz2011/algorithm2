""" To solve the problem of checking if one binary tree (subRoot) is a subtree of another binary tree (root) iteratively,
 we can use a depth-first search (DFS) approach. The idea is to traverse the root tree and, 
at each node, check if the subtree starting from that node matches the subRoot."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not root:
        return False
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        # Check if the current node matches the root of subRoot
        if node.val == subRoot.val:
            if isSameTree(node, subRoot):
                return True
        
        # Push the left and right children onto the stack
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return False

def isSameTree(s: TreeNode, t: TreeNode) -> bool:
    stack = [(s, t)]
    
    while stack:
        node1, node2 = stack.pop()
        
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        
        # Push the children onto the stack
        stack.append((node1.left, node2.left))
        stack.append((node1.right, node2.right))
    
    return True



""" Recursive """
class Solution:
    def isSubtree(self, s,t):
        if not t: return True # if the smaller tree,t  is null then it's definitely a subtree of the bigger tree S
        if not s: return False
        
        if self.sameTree(s,t):
            return True
        else:
            return(self.isSubtree(s.left, t) or
            self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return(self.sameTree(s.left,t.left) and 
            self.sameTree(s.right, t.right))
        return False
