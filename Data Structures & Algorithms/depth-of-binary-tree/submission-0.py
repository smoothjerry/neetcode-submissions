# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node, val):
            if node is None:
                return val
            
            val += 1
            return max(depth(node.left, val), depth(node.right, val))
        
        return depth(root, 0)