class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_count = 0
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                # Update max_count to larger either stack length or keep current
                max_count = max(len(stack), max_count)
                stack.pop()
        return max_count
