class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total_sum = a + nums[l] + nums[r]
                if total_sum < 0:
                    l += 1
                elif total_sum > 0:
                    r -= 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums [l - 1]:
                        l += 1
        return output