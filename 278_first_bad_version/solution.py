""" 
Author: Aarya
Description: You are a product manager and currently leading a team to develop a new product.
  Unfortunately, the latest version of your product fails the quality check.
  Since each version is developed based on the previous version, all the versions after a bad version are also bad.
  Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
  You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version.
  You should minimize the number of calls to the API.
Time Complexity: O(log(n)), This approach uses a binary search algorithm which takes log(n) time.
Space Complexity: O(1), This approach uses a few pointers to keep track of bad versions. Doesn't grow with the input.
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# This class implements a binary search algorithm to find the first bad version among a range of versions.
class Solution:
    """
      This function uses binary search to find the first bad version among a given range of versions.
      
      :param n: The `n` parameter in the `firstBadVersion` function represents the total number of
      versions available. The function uses binary search to find the first bad version among the
      versions from 1 to `n`

      :return: The code is returning the first bad version number within the range of 1 to n.
      """
    def firstBadVersion(self, n: int) -> int:
        L, R = 1, n

        while L <= R:
            mid = (L + R) // 2
            isCurrentVersionBad = isBadVersion(mid)
            isPreviousVersionBad = isBadVersion(mid - 1)

            if isCurrentVersionBad and not isPreviousVersionBad:
                return mid
            elif isCurrentVersionBad:
                R = mid - 1
            else:
                L = mid + 1