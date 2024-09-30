"""
235. Lowest Common Ancestor of a Binary Search Tree
Solved
Medium
Topics
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
 two nodes p and q as the lowest node in T that has both p and q as descendants
   (where we allow a node to be a descendant of itself).”"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # find the ancestors of each node then look for the common lowest
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestorP = self.ancestor(root,p.val)
        ancestorQ = self.ancestor(root,q.val)
        print("ancestorP: ",ancestorP)
        print("ancestorQ: ",ancestorQ)
        result = []
        for i in range( min( len(ancestorQ), len(ancestorP))):
            print("i",i)
            if ancestorP[i] == ancestorQ[i]:
                result.append(ancestorP[i])
        print("Result: ",result)
        return result[-1]

             
    def ancestor(self, root, target):
        if root is None:
            return []
        if root.val == target:
            return [root]

        stack = [(root, [])]  # Stack holds tuples of (current_node, path_to_current)
        
        while stack:
            current, path = stack.pop()
            
            # If we find the target node, return the path (ancestors)
            if current.val == target:
                return path + [current] # +[target] adds the node itself as the lowest ancestor
            
            # Add the current node to the path
            new_path = path + [current]
            
            # Push right and left children to the stack
            if current.right:
                stack.append((current.right, new_path))
            if current.left:
                stack.append((current.left, new_path))
        
        return []  # Return an empty list if the target is not found


        """  ######################### Solution 2 ########################"""
        # since this a BST:
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Start from the root and traverse the tree
        while root:
            # If both p and q are less than root, LCA lies in the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are greater than root, LCA lies in the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # We have found the split point, i.e., the LCA
            else:
                return root
        return None  # In case the root is None