# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new = {}

        def dfs(current):
            if not current:
                return
            if current in old_new:
                current = old_new[current]
                return current
            new = Node(current.val)
            old_new[current] = new
            for adj in current.neighbors:
                new.neighbors.append(dfs(adj))
            return new
        
        return dfs(node)