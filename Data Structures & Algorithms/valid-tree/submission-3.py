class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
    
        visited = set()

        def dfs(current, prev):
            if current in visited:
                return False
            visited.add(current)
            if not graph[current]:
                return True
            for neighbor in graph[current]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, current) == False:
                    return False
            return True
        return dfs(0, -1) and len(visited) == n