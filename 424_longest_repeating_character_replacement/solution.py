class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        output = 0
        character_count = {}

        for r in range(len(s)):
            character_count[s[r]] =  character_count.get(s[r], 0) + 1
            if (r - l + 1) - max(character_count.values()) > k:
                character_count[s[l]] -= 1
                l += 1
            output = max(output, r - l + 1)
        return output