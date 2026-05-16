class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqMap = defaultdict(list)
        for a, b in prerequisites:
            preqMap[a].append(b)
        
        resSet = set()
        order = []
        visited = set()
        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            
            for preq in preqMap[course]:
                if not dfs(preq):
                    return False
            
            visited.remove(course)
            preqMap[course] = []
            if course not in resSet:
                order.append(course)
            resSet.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return order