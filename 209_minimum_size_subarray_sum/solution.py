class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = len(nums) + 1
        l = 0
        current_sum = 0

        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                output = min(output, r - l + 1)
                current_sum -= nums[l]
                l += 1
        return 0 if output == len(nums) + 1 else output