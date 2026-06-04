class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = defaultdict(list)
        for a, b in prerequisites:
            preqs[a].append(b)
        
        visited = set()
        order = set()
        res = []
        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            for pre in preqs[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preqs[course] = []
            if course not in order:
                order.add(course)
                res.append(course)
            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res

    
