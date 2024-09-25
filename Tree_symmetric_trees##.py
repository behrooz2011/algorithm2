"""101. Symmetric Tree
Easy
Topics
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 """
#Iterative:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        # Initialize a queue with the left and right children of the root
        queue = [(root.left, root.right)]

        while queue:
            t1, t2 = queue.pop(0)  # Dequeue the first pair

            # If both nodes are None, continue to the next pair
            if not t1 and not t2:
                continue
            # If one of the nodes is None or their values are not equal, it's not symmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False

            # Enqueue the children in the order that they need to be compared
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True
            

# Recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True

    def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

    return isMirror(root.left, root.right)