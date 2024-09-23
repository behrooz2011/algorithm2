"""
671. Second Minimum Node In a Binary Tree
Solved
Easy
Topics
Companies
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        frequency_dict = {}
        q = []
        q.append(root)
        while q:
            node = q.pop(0)
            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # return result
        print("result: ",result)
        for number in result:
            frequency_dict[number] = 1 + frequency_dict.get(number, 0) #frequency obj
        res = frequency_dict.keys()
        res.sort()
        return (res[1] if len(res) > 1 else -1) #ternary in py