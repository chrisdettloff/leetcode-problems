class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # Base Case: Entire word found
            if i == len(word):
                return True
            # Boundary and match checks
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            # Mark current cell as visited (temporarily)
            board[r][c] = '#'
            # Explore neighbors recursivly in all four directions
            result = any(dfs(r + dr, c + dc, i + 1) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)])
            # Backtrack: Restore the original character
            board[r][c] = word[i]

            return result
        
        # Start DFS if the first letter matches
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
                