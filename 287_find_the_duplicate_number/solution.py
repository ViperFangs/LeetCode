class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cycle_start, fast, slow = 0, 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                while cycle_start != slow:
                    slow = nums[slow]
                    cycle_start = nums[cycle_start]
                return slow