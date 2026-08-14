class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hmap = {}
        for i in range(n):
            hmap[i] = []
        
        for pair in edges:
            hmap[pair[0]].append(pair[1])
            hmap[pair[1]].append(pair[0])
        
        seen = set()
        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)
            for child in hmap[node]:
                if child == prev:
                    continue
                if dfs(child, node) == False:
                    return False
            return True
        
        return dfs(i, -1) and len(seen) == n