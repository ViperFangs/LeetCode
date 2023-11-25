""" 
Author: Aarya
Description: Given an array of integers arr and two integers k and threshold,
    return the number of sub-arrays of size k and average greater than or equal to threshold.
Time Complexity: O(n), where n is the size of the arr
Space Complexity: O(1), The algorithm uses a few variables that don't grow with the input
"""
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Initialize current_sum as 0, this variable stores the sum of the integers inside the window.
        current_sum = 0
        # Initialize a left pointer at 0, this variable will be the start of our window
        l = 0
        # Initialize window length as 0, this variable will be used to the average
        window_length = 0
        # The output variable stores all the number of sub-arrays of size K and average greater than or equal to threshold
        output = 0
        # Loop through the list once using the right pointer
        for r in range(len(arr)):
            # Increase the current sum with the value at the right pointer
            current_sum += arr[r]
            # Increment the length of the window
            window_length += 1
            """
            If the length of the window is bigger than the size of the required sub-array's then
                reduce the current sum by the value at the left pointer
                decrement the length of the window_length
                increment the left pointer
            """
            if window_length > k:
                current_sum -= arr[l]
                window_length -= 1
                l += 1
            """
            if the current window length is less than k then go to the next iteration
                This is done to avoid accidentally increasing the output value if a sub-array of size less than k
                has an average higher than the threshold
            """
            if window_length < k:
                continue
            # If the average of the current window is greater or equal to the threshold then increment the output
            if current_sum / k >= threshold:
                output += 1
        # return the number of sub-arrays of size k and average greater than or equal to threshold.
        return output