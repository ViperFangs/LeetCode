class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)): # for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i