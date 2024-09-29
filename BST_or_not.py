class Solution:
    def isValidBST(self, root):
        res = []
        self.inorder_traversal(root, res)
        return self.is_sorted(res)
        # return sorted(res) == res This is False, for example [2,2,2] is not a bst
    
    def inorder_traversal(self, root, res):
        if root:
            self.inorder_traversal(root.left, res)
            res.append(root.val)
            self.inorder_traversal(root.right, res)
            
    def is_sorted(self, arr):
        if not arr:
            return False
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]: #even equal values are not accepted
                return False
        return True