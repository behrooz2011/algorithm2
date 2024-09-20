class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
class Solution:
    def pre(self,root,result):
        if not root:
            return
        result.append(root.data)
        self.pre(root.left,result)
        self.pre(root.right,result)
        return(result)
r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.right = Node(100)


#j=Solution()
print(Solution().pre(r,[]))
""" [1, 2, 4, 5, 3, 100] """