class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Handle edge case
        if k <= 1:
            return 0
        
        left = 0
        right = 0
        product = 1
        count = 0

        while right < len(nums):
            product *= nums[right]
            # Shrink window if product exceeds k
            while product >= k and left <= right: 
                product //= nums[left]
                left += 1
            # All subarrays ending at right are valid
            count += right - left + 1
            right += 1
        return count