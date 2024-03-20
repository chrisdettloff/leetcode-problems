class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Traverse list1 to find just before the start of the merge
        current = list1
        i = 0
        while i < a - 1:
            current = current.next
            i += 1

        head = current # Store the node before the merge start 

        # Travse list1 to find the end of the merge section
        while i <= b:
            current = current.next
            i += 1

        head.next = list2 # Connect the node before the merge start to start of list 2

        # Find end of list2
        while list2.next:
            list2 = list2.next

        list2.next = current # Connect end of list2 to the node after the merge section in list1
        return list1