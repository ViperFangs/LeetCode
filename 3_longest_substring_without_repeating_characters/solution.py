class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            l = 0
            window = set()
            max_length = 0

            for r in range(len(s)):
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
                max_length = max(len(window), max_length)
            return max_length