# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        index = 0
        root = TreeNode(preorder[0])
        for idx, num in enumerate(inorder):
            if root.val == num:
                index = idx
        
        root.left = self.buildTree(preorder[1:index + 1], inorder[0:index])
        root.right = self.buildTree(preorder[index + 1:len(inorder)], inorder[index + 1:len(inorder)])
        return root