

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_ancestors(root, target):
    if root is None:
        return []

    stack = [(root, [])]  # Stack holds tuples of (current_node, path_to_current)
    
    while stack:
        current, path = stack.pop()
        
        # If we find the target node, return the path (ancestors)
        if current.value == target:
            return path
        
        # Add the current node to the path
        new_path = path + [current.value]
        
        # Push right and left children to the stack
        if current.right:
            stack.append((current.right, new_path))
        if current.left:
            stack.append((current.left, new_path))
    
    return []  # Return an empty list if the target is not found

# Example usage:
# Constructing a binary tree
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
#
root.left.right.left = TreeNode(50)
root.left.right.right = TreeNode(60)

target = 60
ancestors = get_ancestors(root, target)
print(ancestors)  # Output: [1, 2] if target = 4