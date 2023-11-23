""" 
Author: Aarya
Description: You are given an integer array height of length n. 
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
Time Complexity: O(n), where n is the size of the height list
Space Complexity: O(1), The algorithm only initializes a few extra integers
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the left pointer at the start and the right pointer at the end of the height list
        l, r = 0, len(height) -1
        # Initialize the max_area, this will be returned at the end
        max_area = 0
        # loop until the left pointer is greater then the right pointer
        while l < r:
            """
            calculate the current area using (width * height)
            we use the minimum value of height as that's our bottleneck
            """
            current_area = (r - l) * min(height[l], height[r])
            # store the bigger area between the current_area and the stored max_area in max_area
            max_area = max(max_area, current_area)
            # Increment the left pointer by one if the value at the left pointer is less than the value at the right pointer 
            if height[l] < height[r]:
                l += 1
            # Decrement the right pointer if the value at the right pointer is less than or equal to the value at the left pointer
            else :
                r -= 1
        # return the max_area that was calculated
        return max_area