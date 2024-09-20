class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
class Solution:
    def preOrderIte(self, root, result):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(Solution().preOrderIte(root,[]))
""" [1, 2, 4, 5, 3, 6, 7] """