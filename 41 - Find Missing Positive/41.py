class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Handle non-positives by moving out of range(n)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # Mark number as seen
        for i in range(n):
            if abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        # Largest positive number + 1 is answer
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1 