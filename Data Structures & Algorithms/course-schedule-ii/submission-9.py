class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = defaultdict(list)
        for a, b in prerequisites:
            preqs[a].append(b)

        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            for b in preqs[course]:
                if not dfs(b):
                    return False
            visited.remove(course)
            
            preqs[course] = []
            order[course] = True

            return True
        
        visited = set()
        order = {}
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return list(order.keys())

    
