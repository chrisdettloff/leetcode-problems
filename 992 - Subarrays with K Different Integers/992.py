class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(nums, k):
            count = distinct_count = left = 0
            seen = {}

            for right, num in enumerate(nums):
                seen[num] = seen.get(num, 0) + 1
                if seen[num] == 1:
                    distinct_count += 1

                while distinct_count > k:
                    seen[nums[left]] -= 1
                    if seen[nums[left]] == 0:
                        distinct_count -= 1
                    left += 1

                count += right - left + 1
            return count
        return at_most_k(nums, k) - at_most_k(nums, k - 1)
