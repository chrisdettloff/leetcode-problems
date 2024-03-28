class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        freq = defaultdict(int)
        max_length = 0
        for right in range(len(nums)):
            # Increment frequency of current element in the hashmap
            freq[nums[right]] += 1
            # Shrink the window if current element violates the k rule
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            # Update max_length if necessary
            max_length = max(max_length, right - left + 1)
        return max_length