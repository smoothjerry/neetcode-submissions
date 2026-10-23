# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(float("-inf"), root, float("inf"))
    
    def valid(self, leftVal, node, rightVal): 
        if not node:
            return True
        
        if not(leftVal < node.val < rightVal):
            return False
        
        left = self.valid(leftVal, node.left, node.val)
        right = self.valid(node.val, node.right, rightVal)
        return left and right
