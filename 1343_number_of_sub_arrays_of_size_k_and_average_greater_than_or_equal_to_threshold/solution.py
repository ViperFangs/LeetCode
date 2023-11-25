class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = 0
        l = 0
        window_length = 0
        output = 0

        for r in range(len(arr)):
            current_sum += arr[r]
            window_length += 1
            if window_length > k:
                current_sum -= arr[l]
                l += 1
            if window_length < k:
                continue
            if current_sum / k >= threshold:
                output += 1
        return output