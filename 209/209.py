class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None  # Initialize 'prev' pointer to None, representing the start of the reversed list

        while head:  # Loop as long as there's a current node ('head')
            temp = head.next  # Store the next node temporarily
            head.next = prev  # Reverse the current node's pointer to the previous node
            prev = head  # Move the 'prev' pointer forward to the current node
            head = temp  # Move the 'head' pointer to the next node for the next iteration

        return prev  # After the loop, 'prev' points to the new head of the reversed list
