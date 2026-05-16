class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] -= 1
        
        q = deque()
        readyTasks = [val for val in counts.values()] 
        heapq.heapify(readyTasks)
        time = 0
        while q or readyTasks:
            if readyTasks:
                task = heapq.heappop(readyTasks)
                task += 1
                if task != 0:
                    q.append((task, time + n))
            
            if q:
                if time >= q[0][1]:
                    task, _ = q.popleft()
                    heapq.heappush(readyTasks, task)
            
            time += 1
        
        return time

