class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        for a, b in prerequisites:
            preqs[a].append(b)

        def dfs(i):
            if i in visited:
                return False
            
            visited.add(i)
            for b in preqs[i]:
                if not dfs(b):
                    return False
            visited.remove(i)
            
            return True
        
        for i in range(numCourses):
            visited = set()
            if not dfs(i):
                return False
        
        return True