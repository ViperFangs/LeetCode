""" 
Author: Aarya
Description: You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Time Complexity: O(n), where n is the size of the prices list
Space Complexity: O(1), The algorithm creates a couple variables to hold the pointers
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the left pointer at the start
        l = 0
        # Initialize the max profit as 0
        max_profit = 0
        # Loop through the prices list, the right pointer starts at index 1
        for r in range(1 ,len(prices)):
            # if the value at the right pointer is less than the value at the left pointer then update the left pointer to the right pointer
            if prices[r] < prices[l]:
                l = r
            # update the max_profit if the value at the right pointer - the value at the left pointer is greater than the current max_profit
            max_profit = max(prices[r] - prices[l], max_profit)
        # return the max profit
        return max_profit