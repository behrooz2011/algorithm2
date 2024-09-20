class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
class Solution:
    def postOrder(self, root, result):
        if not root:
            return
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.data)
        return result
        
r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.left = Node(6)
r.right.right = Node(7)

print(Solution().postOrder(r,[]))
""" [4, 5, 2, 6, 7, 3, 1] """