class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            # If stack is not empty and last letter is opposite case of current
            if stack and stack[-1] == i.swapcase():
                stack.pop()
            else:
                stack.append(i)
        # Handle empty string
        return "".join(stack)
