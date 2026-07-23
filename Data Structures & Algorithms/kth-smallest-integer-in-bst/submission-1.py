# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        self.helper(root, heap)

        for i in range(k - 1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
    def helper(self, root: Optional[TreeNode], heap):
        if not root:
            return
        heapq.heappush(heap, root.val)
        self.helper(root.left, heap)
        self.helper(root.right, heap)