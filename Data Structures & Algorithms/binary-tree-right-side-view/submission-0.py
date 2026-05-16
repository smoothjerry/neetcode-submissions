# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue, res = deque(), []
        queue.append(root)
        while queue:
            size = len(queue)
            while size > 1:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            rightmost = queue.popleft()
            if rightmost.left:
                queue.append(rightmost.left)
            if rightmost.right:
                queue.append(rightmost.right)
            res.append(rightmost.val)
        
        return res