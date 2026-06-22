# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root, arr):
            if not root:
                return
            helper(root.left, arr)
            arr.append(root.val)
            helper(root.right, arr)
        array = []
        helper(root, array)

        return array[k - 1]