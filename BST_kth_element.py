# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: #preorder
            return
        stack = []
        stack.append(root)
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        arr = self.helper(result)
        return arr[k-1]


    def helper(self,arr): #freq counter
        arr.sort()
        count = {}
        for x in arr:
            count[x] = 1 + count.get(x,0)
        keys = count.keys()
        return keys
        

############# Second Solution: without Freq counter ##############
class Solution:
    def kthSmallest(self, root, k):
        arr = self.inorder(root,[])
        return arr[k-1]
    
    def inorder(self, root, arr):
        if not root:
            return 
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
        return arr