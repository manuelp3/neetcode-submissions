class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {}
        for i in range(numCourses):
            course_map[i] = []

        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            course_map[course].append(prereq)
        
        visit_set = set()

        def dfs(value):
            if not course_map[value]:
                return True
            if value in visit_set:
                return False
            visit_set.add(value)
            for prereq in course_map[value]:
                if not dfs(prereq):
                    return False
            visit_set.remove(value)
            course_map[value] = []
            return True
    
        for key in course_map:
            if not dfs(key):
                return False
        return True