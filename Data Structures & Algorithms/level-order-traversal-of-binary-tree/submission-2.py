# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        # if not root:
        #     return
        # #res.append([root.val])
        # curr = root

        # q = deque()
        # q.append(curr)
        # while q:
        #     node = q.popleft()
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        #     #res.append(q)
        # print(res)
        # return res
        arr = []
        self.helper(root, 0, arr)
        bucket = [[] for _ in range(len(arr))]

        for pair in arr:
            index = pair[1]
            value = pair[0]
            bucket[index].append(value)
        print(bucket)

        res = []

        for lis in bucket:
            if lis:
                res.append(lis)
        print(res)
        return res
    def helper(self, root: Optional[TreeNode], height, arr: List):
        if not root:
            return
        #print(root.val, height)
        arr.append([root.val, height])
        self.helper(root.left, 1 + height, arr)
        self.helper(root.right, 1 + height, arr)