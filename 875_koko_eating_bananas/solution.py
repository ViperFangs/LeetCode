""" 
Author: Aarya
Description: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
    The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour eating speed of k. 
    Each hour, she chooses some pile of bananas and eats k bananas from that pile.
        If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
    Return the minimum integer k such that she can eat all the bananas within h hours.
Time Complexity: O(log(n)), The algorithm utilizes a binary search solution which has a time complexity of log(n).
    Note: n here represents the largest number in the pile -> max(piles)
Space Complexity: O(1), The algorithm only uses a few pointers that dont grow with the input.
Logic: The logic here is that len(piles) <= h. That means koko can eat the largest number of bananas in the pile every hour 
    and it will be guaranteed to be less than h. Therefore the effective search range become 1 to max(piles).
    We can then utilize binary search algorithm on the search range
    and find the minimum number of bananas that can be eaten per hour.
"""

# This class calculates the minimum eating speed required to eat all piles within a given time limit.
class Solution:
    """
    The function `minEatingSpeed` calculates the minimum eating speed required to eat all piles
    within a given number of hours using binary search.
    
    :param piles: The `piles` parameter is a list of integers representing the number of bananas in
    each pile

    :param h: The parameter `h` represents the maximum number of hours within which the piles of
    bananas need to be eaten. 

    :return: the minimum integer value representing the eating speed required to eat all the piles
    within h hours.
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The binary search range is from 1 to max(piles)
        L, R = 0, max(piles)
        result = R

        while L <= R:
            mid = (L + R) // 2
            hours = 0

            # Go through each pile find the total number of hours 
            # required to finish eating at the speed of `mid` bananas every hour
            for p in piles:
                hours += math.ceil(p / mid)
            # If the hours required to finish all the piles is less than h,
            # then update the result to mid.
            if hours <= h:
                result = mid
                # Search is the lower half of the range to see if there is a faster speed.
                R = mid - 1
            # If the hours required to finish all the piles is more than h,
            # then increase of the number of bananas that can be eaten each hour.
            else:
                # Search is the upper half of the range to see if there is a speed 
                # that can eat all bananas is less than `h`` hours.
                L = mid + 1
        
        return result