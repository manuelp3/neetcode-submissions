# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        num = root
        while num:
            if p.val < num.val and q.val < num.val:
                num = num.left
            elif p.val > num.val and q.val > num.val:
                num = num.right
            else:
                return num
        return num