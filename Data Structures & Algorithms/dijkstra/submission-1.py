class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((w, d))
        
        shortest = {}
        heap = [(0, src)]
        while heap:
            w, node = heapq.heappop(heap)
            if node in shortest:
                continue
            
            shortest[node] = w

            for wei, nei in adj[node]:
                if nei not in shortest:
                    heapq.heappush(heap, (wei + w, nei))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest