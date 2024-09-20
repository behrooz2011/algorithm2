class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
class Solution:
    def postOrder(self, root, result):
        if not root:
            return
        visited = set()
        stack = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and node.right not in visited:
                    stack.append(node)
                    node = node.right
                else:
                    result.append(node.data)
                    visited.add(node)
                    node = None
        return result
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(Solution().postOrder(root, []))
""" [4, 5, 2, 6, 7, 3, 1] """