class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[L] = nums[i]
                L += 1
        return L