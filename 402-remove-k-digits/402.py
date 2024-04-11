class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        # Keep largest digit in stack
        for i in num:
            while stack and k > 0 and i < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)

        # Remove leading zeros
        stack = stack[:-k] if k > 0 else stack

        # Reconstruct number from stack
        result = "".join(stack).lstrip("0")

        # Return 0 if empty stack
        return result if result else "0"
