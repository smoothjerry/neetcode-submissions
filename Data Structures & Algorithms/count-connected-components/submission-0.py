class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # iterate over all nodes
        # a full traversal signifies one connected component
        # numConnectedComponents == number of traversals we end up doing
        adjList = collections.defaultdict(list)
        for node, edge in edges:
            adjList[node].append(edge)
            adjList[edge].append(node)
        
        # visited set to track per-traversal cycles
        # component set to track nodes that have been completed already
        # for all nodes:
        numComponents = 0
        visited = set()
        def bfs(node):
            queue = deque()
            queue.append(node)
            visited.add(node)
            while queue:
                current = queue.popleft()
                for nei in adjList[current]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

        for node in range(n):
            if node not in visited:
                bfs(node)
                numComponents += 1
        
        return numComponents
