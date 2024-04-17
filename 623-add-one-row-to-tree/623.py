class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:  
                # Special Case: If we need to insert at the top, create a new root  
            return TreeNode(val, root, None)  # New root with the old tree as left child

        queue = [(root, 1)]  # Store (node, current_level) pairs for BFS
        while queue:
            node, curr_depth = queue.pop(0)  # Get the next node and its depth
            if curr_depth == depth - 1:  # If we're one level above the desired depth:
                # Create new left and right nodes with the specified value
                node.left = TreeNode(val, node.left, None) 
                node.right = TreeNode(val, None, node.right)

            else:  # Keep traversing down the tree
                if node.left: queue.append((node.left, curr_depth + 1))
                if node.right: queue.append((node.right, curr_depth + 1))

        return root  # Return the modified tree 