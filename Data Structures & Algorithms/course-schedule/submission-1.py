class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        for a, b in prerequisites:
            preqs[a].append(b)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            for pre in preqs[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preqs[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True