# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lbound = TreeNode(float("-inf"))
        rbound = TreeNode(float("inf"))

        return self.helper(root, lbound, rbound)

    def helper(self, root: Optional[TreeNode], lbound: Optional[TreeNode], rbound: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.val > lbound.val and root.val < rbound.val:
            return self.helper(root.left, lbound,root) and self.helper(root.right, root, rbound)
        else:
            return False
        return True