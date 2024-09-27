# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        q = [root]
        while q:
            node = q.pop(0)
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            
            # Add children to the queue for further processing
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        # return root

        #### Solution 2 #########
        # if not root:
        #     return None
        
        # # Swap the left and right children
        # root.left, root.right = root.right, root.left
        
        # # Recursively invert the left and right subtrees
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        
        # return root
