class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
class Solution:
    def Inorder(self, root, result):
        if not root:
            return
        self.Inorder(root.left,result)
        result.append(root.data)
        self.Inorder(root.right, result)
        return result
r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left  = Node(4)
r.left.right = Node(5)
r.right.left = Node(6)
r.right.right = Node(7)

print(Solution().Inorder(r,[]))
""" [4, 2, 5, 1, 6, 3, 7] """