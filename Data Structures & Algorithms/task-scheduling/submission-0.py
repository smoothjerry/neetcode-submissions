class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.defaultdict(int)
        for task in tasks:
            counts[task] -= 1
        
        heap = [ x[1] for x in counts.items() ]
        heapq.heapify(heap)

        time = 0
        queue = deque()
        while heap or queue:
            time += 1
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task != 0:
                    cooldown = time + n
                    queue.append([task, cooldown])
            
            if queue:
                task, cooldown = queue[0]
                if cooldown <= time:
                    queue.popleft()
                    heapq.heappush(heap, task)
        
        return time

