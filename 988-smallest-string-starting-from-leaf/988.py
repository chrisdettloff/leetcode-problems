class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return

            path.append(chr(node.val + ord('a')))  # Add letter to path

            if not node.left and not node.right:  # Leaf node
                nonlocal answer
                path_str = ''.join(path[::-1])  # Reverse for leaf-to-root
                answer = min(answer, path_str)

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()  # Backtrack

        answer = "zzzzzzzzzz"  # Initialize with a large string
        dfs(root, [])
        return answer