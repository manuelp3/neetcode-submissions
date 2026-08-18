class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class_map = {}

        for i in range(numCourses):
            class_map[i] = []

        for course, prereq in prerequisites:
            class_map[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if class_map[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in class_map[course]:
                if dfs(prereq) == False:
                    return False
            class_map[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True