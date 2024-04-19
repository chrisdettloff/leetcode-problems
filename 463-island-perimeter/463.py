class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # If it's a land cell
                    # Check neighbors:
                    perimeter += 4  # Assume 4 sides initially
                    if i > 0 and grid[i - 1][j] == 1: perimeter -= 1  # Top
                    if i < rows - 1 and grid[i + 1][j] == 1: perimeter -= 1  # Bottom
                    if j > 0 and grid[i][j - 1] == 1: perimeter -= 1  # Left
                    if j < cols - 1 and grid[i][j + 1] == 1: perimeter -= 1  # Right

        return perimeter