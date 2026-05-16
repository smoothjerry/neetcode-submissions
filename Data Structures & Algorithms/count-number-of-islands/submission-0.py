class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        def bfs(row, col):
            print("row:", row, "col:", col, "val:", grid[row][col])
            if (row, col) in visited or grid[row][col] == '0':
                print("value:", (row, col))
                return 0
            
            visited.add((row, col))
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for x, y in dirs:
                    nextR = r + x
                    nextC = c + y
                    if 0 <= nextR < len(grid) and 0 <= nextC < len(grid[0]) and (nextR, nextC) not in visited and grid[nextR][nextC] == '1':
                        visited.add((nextR, nextC))
                        queue.append((nextR, nextC))
            return 1
        
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                numIslands += bfs(i, j)
        
        return numIslands
