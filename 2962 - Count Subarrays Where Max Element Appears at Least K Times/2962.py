class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        right = 0

        while right < len(nums):
            k -= nums[right] == max(nums)
            right += 1
            while k == 0:
                k += nums[left] == max(nums)
                left += 1
            result += 1
        return result