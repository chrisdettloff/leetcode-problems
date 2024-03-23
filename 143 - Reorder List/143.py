class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Create a deque to store all nodes of the list, facilitating access from both ends
        q = deque() 

        # Create a temporary head node to simplify traversal 
        temp = ListNode(0)
        temp.next = head
        curr = temp.next

        # Store all nodes in the deque
        while curr:
            q.append(curr)
            curr = curr.next

        # Re-link nodes: start with the temporary head node 
        curr = temp
        even = False  # Flag to alternate between popping from the left and right of the deque 

        # Interleave nodes from the front and end of the deque
        while q:
            if even:
                node = q.pop()       # Take a node from the end
            else:
                node = q.popleft()   # Take a node from the front

            node.next = None         # Break any existing 'next' connections
            curr.next = node         # Attach the node to the re-ordered list
            curr = curr.next         # Move to the next position for the next node
            even ^= True             # Toggle the 'even' flag for the next iteration
