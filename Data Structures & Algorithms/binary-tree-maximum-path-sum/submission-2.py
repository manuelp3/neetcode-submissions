# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal = root.val

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            left = max(left, 0)
            right = max(right, 0)

            self.maxVal = max(self.maxVal, left + root.val + right)

            return root.val + max(left, right)
        
        dfs(root)
        return self.maxVal