# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.string = ""
        def dfs(root):
            if not root:
                self.string += "n"
                self.string += ","
                return
            else:
                self.string += str(root.val)
                self.string += ","
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(self.string)
        return self.string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        self.start = 0
        self.end = 0
        
        def dfs(root):
            root = TreeNode(0)
            while data[self.end] != ',' and self.end < len(data):
                self.end += 1
            value = data[self.start:self.end]
            if value == 'n':
                self.end += 1
                self.start = self.end
                return None
            else:
                root.val = int(value)
            self.end += 1
            self.start = self.end
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root

        return dfs(None)