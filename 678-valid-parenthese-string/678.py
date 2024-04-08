class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []  # Additional stack to track positions of '*'

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Record the position of '('
            elif char == '*':
                star_stack.append(i)  # Record the position of '*'
            elif char == ')':
                if stack:  # Prioritize matching '(' 
                    stack.pop()
                elif star_stack:  # If no '(', use '*' as ')'
                    star_stack.pop()
                else:  # No '(' or '*' to match
                    return False

        # Handle remaining open parentheses with '*' 
        while stack and star_stack:
            if stack.pop() > star_stack.pop():
                # '*' is positioned before '(', invalid
                return False

        return not stack  # Stack should be empty for validity