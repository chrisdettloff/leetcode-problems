class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            index = abs(num) - 1
            # Already visited
            if nums[index] < 0:
                res.append(abs(num))
            # Mark as visited
            nums[index] = -nums[index]
        return res