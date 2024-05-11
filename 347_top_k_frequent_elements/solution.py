""" 
Author: Aarya
Description: Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.
Time Complexity: O(n) where n is the size of nums
Space Complexity: O(n), where N is the number of unique elements in the input list
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap that will store the key as the number and value as the amount of times(count) it appears in the nums list
        hashmap = {}
        # create a list that will store k most frequent elements
        result = []
        """
        create a 2D list that will store the count as the index and all the keys with that count as the value
        e.g. for [1,1,1,2,2,2,3,3,4], frequency will be [[], [4], [3], [1, 2], [], [], []]
            1 and 2 appear 3 times in the nums list, it will be stored at the 3rd index
            3 appears 2 times in the nums list, it will be stored at the 2nd index
            4 appears 1 time in the nums list, it will be stored in the first index
        """
        frequency = []
        """
        add empty lists to the frequency list
        the max index for the frequency list is the length of nums + 1.
        this is because even if the list consists of the same element, the count of the element will not exceed the number of items in the nums list
        """
        for i in range(len(nums) + 1):
            frequency.append([])
        # populate the hashmap with the num as the key and the value as the amount of times(count) the key appears in the nums list.
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        # use value(which stores the count) of each key as the index for the 2d frequency list, and append the key to the list at that index
        for key, val in hashmap.items():
            frequency[val].append(key)
        """
        loop through the frequency list in backwards order, as the highest count will be at the end of the list
        loop till the first element because the 0th index is not going to be populated.
        """
        for i in range(len(frequency) - 1, 0, -1):
            # loop through each element at the current index if the list has elements
            for n in frequency[i]:
                # if the list has elements, then append it to the result list
                result.append(n)
                """
                after appending an element to the list, check the length of the result list and compare it to k
                if the length of the result list is the same as k, then return the result as it will contain the k most frequent elements
                """
                if len(result) == k:
                    return result
        