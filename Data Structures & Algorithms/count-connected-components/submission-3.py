class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_map = {}

        for i in range(n):
            node_map[i] = []
        
        for pair in edges:
            first = pair[0]
            second = pair[1]
            node_map[first].append(second)
            node_map[second].append(first)
        
        union = [False] * n
        
        self.res = 0

        def dfs(node):
            if union[node]:
                return
            union[node] = True
            for child in node_map[node]:
                dfs(child)
        
        for i in range(n):
            if not union[i]:
                dfs(i)
                self.res += 1
        return self.res
        