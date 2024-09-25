"MAXIMUM depth of a tree"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """ Solution 1: Iterative"""
        # if not root:
        #     return 0
        
        # result = []
        # queue = [root]  # Using a list to simulate a queue
        
        # while queue:
        #     level = []
        #     next_queue = []  # Temporary list to store the next level nodes
            
        #     for node in queue:
        #         if node:
        #             level.append(node.val)
        #             next_queue.append(node.left)  # Add left child (can be None)
        #             next_queue.append(node.right)  # Add right child (can be None)
        #         else:
        #             level.append("null")
        #             next_queue.append(None)  # For the left child of "null"
        #             next_queue.append(None)  # For the right child of "null"
            
        #     # Check if the level is all "nulls" (to break early if the tree is complete)
        #     if all(x == "null" for x in level):
        #         break
            
        #     result.append(level)
        #     queue = next_queue  # Move to the next level
        
        # return len(result)

        ########### Solution 2 ################
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        