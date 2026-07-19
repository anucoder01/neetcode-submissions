class Solution:
    def reorderList(self, head):

        if not head or not head.next:
            return

        # Step 1: Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        # Step 3: Merge
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2