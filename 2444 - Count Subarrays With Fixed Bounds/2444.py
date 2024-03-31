class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        badi = mini = maxi = -1  # Initialize tracking variables

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                badi = i  # Update 'badi' to the index of the invalid element

            if nums[i] == minK:
                mini = i  # Update 'mini' to the index of the latest 'minK'

            if nums[i] == maxK:
                maxi = i  # Update 'maxi' to the index of the latest 'maxK'

            # Calculate subarrays ending at the current index, ensuring window validity
            if mini >= 0 and maxi >= 0 and badi < min(mini, maxi):
                ans += min(mini, maxi) - badi + 1  

        return ans