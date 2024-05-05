"""
Author: Aarya
Description: Write a function that takes the binary representation of a positive integer 
  and returns the number of set bits it has (also known as the Hamming weight).
Time Complexity: O(1), The given number is going to take 32 bits. 
  So in the worst case, the algorithm will only perform 32 operations which takes constant time.
Space Complexity: O(1), the code uses an integer to keep track of number of one bits
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            # Utilize the AND operator to see if the binary value of n && 1 == 1.
            # By definition, n & 1 = n.
            # This operation just checks to see if the right most bit is a one or not
            # If the right most bit is 1 then the if statement will evaluate to true
            #  Then we increase the count
            if n & 1 == 1:
                count += 1
            # Use the right bit shift operator to shift all the bits by 1
            n = n >> 1
        # Once n becomes all zeros, we can return the number of 1 bits present in n
        return count