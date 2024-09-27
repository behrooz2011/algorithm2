""" 
####################### BST ############################
A Binary Search Tree is a data structure used in computer science for organizing and storing data
in a sorted manner. Each node in a Binary Search Tree has at most two children, a left child and a right child,
with the left child containing values less than the parent node and the right child containing values greater than 
the parent node. 
This hierarchical structure allows for efficient searching, insertion, and deletion operations on the data stored
in the tree.
########################################################

To convert a sorted integer array into a height-balanced binary search tree (BST),
 you can use a recursive approach. The idea is to choose the middle element of the array as the root of the tree, 
 and then recursively do the same for the left and right subarrays 
to create the left and right subtrees."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2  # Find the middle index
    root = TreeNode(nums[mid])  # Create a node with the middle element

    # Recursively build the left and right subtrees
    root.left = sortedArrayToBST(nums[:mid])  # Left subarray
    root.right = sortedArrayToBST(nums[mid + 1:])  # Right subarray

    return root
nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
"""
########### Iteratively ##############
use a stack to simulate the recursive behavior. 
The idea is to keep track of the subarrays that need to be processed and build the tree level by level.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    # Create a stack to hold the tuples of (start, end) indices
    stack = [(0, len(nums) - 1)]
    # Create a placeholder for the root node
    root = None
    # This will hold the nodes to connect to the tree
    nodes = []

    while stack:
        start, end = stack.pop()
        if start > end:
            continue
        
        mid = (start + end) // 2  # Find the middle index
        node = TreeNode(nums[mid])  # Create a new node with the middle element
        
        if not nodes:
            root = node  # The first node becomes the root
        else:
            # Connect the new node to the last node in the list
            if mid < nodes[-1].val:  # If mid is less than the last node's value, it goes to the left
                nodes[-1].left = node
            else:  # Otherwise, it goes to the right
                nodes[-1].right = node
        
        # Add the new node to the list of nodes
        nodes.append(node)
        
        # Push the right and left subarrays onto the stack
        stack.append((mid + 1, end))  # Right subarray
        stack.append((start, mid - 1))  # Left subarray

    return root
