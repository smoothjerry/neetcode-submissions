class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        freshOranges = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        minutes = 0
        while queue and freshOranges > 0:
            size = len(queue)
            for _ in range(size):
                rottenRow, rottenCol = queue.popleft()
                for x, y in DIRS:
                    nextRow = rottenRow + x
                    nextCol = rottenCol + y
                    if 0 <= nextRow < ROWS and 0 <= nextCol < COLS and grid[nextRow][nextCol] == 1:
                        grid[nextRow][nextCol] = 2
                        freshOranges -= 1
                        queue.append((nextRow, nextCol))
            minutes += 1

        return minutes if freshOranges == 0 else -1