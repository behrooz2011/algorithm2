"Same tree"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = [(p, q)]
        
        while queue:
            # Dequeue the first pair of nodes
            node1, node2 = queue.pop(0)
            
            # If both nodes are None, continue to the next pair
            if not node1 and not node2:
                continue
            
            # If one of the nodes is None or their values are different, return False
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Enqueue the children of both nodes
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        # If we finish the loop without returning False, the trees are the same
        return True


#### Solution 2: Recursive: ######
class Solution:
    def sameTree(self, p, q):
        # Base case: both nodes are None
        if not p and not q:
            return True
        # If one of the nodes is None, or the values are different
        if not p or not q or p.val != q.val:  # Use p.val if your node class uses 'val'
            return False
        # Recursively check the left and right subtrees and combine results
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

p1 = Node(1)
p1.left = Node(2)
p1.right = Node(3)
p1.left.left = Node(4)
p1.left.right = Node(5)

q1 = Node(1)
q1.left = Node(2)
q1.right = Node(3)
q1.left.left = Node(4)
q1.left.right = Node(5)

p2 = Node(1)
p2.left = Node(2)

q2 = Node(1)
q2.right = Node(2)