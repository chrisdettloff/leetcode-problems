class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = []
        y = []
        # Append value of current node to list
        while head:
            x.append(head.val)
            head = head.next
        # Reverse list and store in new list
        y = x[::-1]
        return x == y
