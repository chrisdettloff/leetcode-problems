class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        # Find intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # Cycle Exists
            if slow == fast:
                break
        # Find the start of the cycle(duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        # Meeting point is the duplicate
        return slow