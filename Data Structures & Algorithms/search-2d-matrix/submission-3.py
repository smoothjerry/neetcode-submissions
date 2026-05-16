class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        lo, hi = 0, (M * N) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            row, col = mid // N, mid % N
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
        


