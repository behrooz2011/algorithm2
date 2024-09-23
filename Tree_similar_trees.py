"""100. Same Tree
Solved
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."""

"""
        1          1
       /     !=      \ 
      2                2
"""


"Iterative"
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = []
        queue.append((p, q))
        
        while queue:
            # Dequeue the first pair of nodes
            node1, node2 = queue.pop(0)
            
            # If both nodes are None, continue to the next pair
            if not node1 and not node2:
                continue
            
            # If one of the nodes is None or their values are different, return False
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Enqueue the children of both nodes
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        # If we finish the loop without returning False, the trees are the same
        return True
    

" recursive"
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # If both nodes are None, they are the same
    if not p and not q:
        return True
    # If one of the nodes is None, or the values are different, they are not the same
    if not p or not q or p.val != q.val:
        return False
    # Recursively check the left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Example usage:
# Tree 1:    1
#           /   \
#          2     3
# Tree 2:    1
#           /   \
#          2     3
# p = TreeNode(1, TreeNode(2), TreeNode(3))
# q = TreeNode(1, TreeNode(2), TreeNode(3))
# print(isSameTree(p, q))  # Output: True