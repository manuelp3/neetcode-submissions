# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = []

        def dfs(root):
            if not root:
                string.append("n")
                return
            string.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(string)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        string = data.split(",")
        #print(string)
        self.index = 0

        def dfs():
            if string[self.index] == 'n':
                self.index += 1
                return None
            root = TreeNode(int(string[self.index]))
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        root = dfs()
        return root
        