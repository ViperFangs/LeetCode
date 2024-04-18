class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        L = 0
        R = (M * N) - 1

        while L <= R:
            mid = (L + R) // 2
            i = mid // N
            j = mid % N

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                R = mid - 1
            else:
                L = mid + 1
        
        return False        