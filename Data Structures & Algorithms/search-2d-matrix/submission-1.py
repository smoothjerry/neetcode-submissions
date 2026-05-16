class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        lo, hi = 0, M - 1
        pivot = -1
        while lo <= hi:
            mid = (hi + lo) // 2
            row = matrix[mid]

            if row[0] <= target <= row[N - 1]:
                pivot = mid
                break
            
            elif target < row[0]:
                hi = mid - 1
            
            else:
                lo = mid + 1
            
        if pivot == -1:
            return False

        lo, hi = 0, N - 1
        row = matrix[pivot]
        while lo <= hi:
            mid = (lo + hi) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
        


