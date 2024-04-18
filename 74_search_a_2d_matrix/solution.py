""" 
Author: Aarya
Description: 
Time Complexity: O(log(M * N)), where M is the size of the row and N is the size of the columns
Space Complexity: O(1), we only use a few integers which don't grow with the size of the input 
Logic: The logic here is to perform a binary search but the twist is to convert a 1d index into a 2d index
  by using the properties of division and modulus operators.
  This works because the size of columns is the same.
  Eg: If M = 3, N = 4, L = 0, R = 11, i = index // N, j = index % N
    Index [5] is converted to [1][1], i = 5 // 4 = 1, j = 5 % 4 = 1  
    Index [2] is converted to [0][2], i = 2 // 4 = 0, j = 2 % 4 = 2
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find the size of M and N (row and columns) using the len() method
        M = len(matrix)
        N = len(matrix[0])
        # Initialize a left pointer at the start of the 2d matrix
        L = 0
        # Initialize a right pointer at the end of the 2d matrix
        R = (M * N) - 1
        # Perform binary search on the 2d matrix
        while L <= R:
            # Find the mid index
            mid = (L + R) // 2
            # Convert the mid index (1d index) into a 2d index by using division and modulus properties
            i = mid // N
            j = mid % N
            # Return true if the value at the current index is equal to the target
            if matrix[i][j] == target:
                return True
            # Change the Left and Right pointer depending on the target and the value at the mid index
            elif matrix[i][j] > target:
                R = mid - 1
            else:
                L = mid + 1
        # Return False if the algorithm hasn't returned True by now as the target doesn't exist in the 2d matrix.
        return False        