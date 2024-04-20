# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
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