class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()
        result = []

        # push opening parentheses into a stack
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                # if stack is empty the closing parenthesis is invalid
                if not stack:
                    remove_indices.add(i)
                else:
                    stack.pop()

        # add indices of unmatched open parentheses
        remove_indices |= set(stack)

        for i, char in enumerate(s):
            if i not in remove_indices:
                result.append(char)

        return "".join(result)
