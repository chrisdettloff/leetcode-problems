class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_area = 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area


def largestRectangleArea(heights):
    max_area = 0
    stack = []

    heights.append(0)  # Adding a sentinel height to trigger remaining calculations

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area