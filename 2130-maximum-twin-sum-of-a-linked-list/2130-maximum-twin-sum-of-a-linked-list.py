class Solution(object):
    def pairSum(self, head):
        slow = fast = head

        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Calculate the maximum twin sum
        maximum = 0
        first = head
        second = prev

        while second:
            maximum = max(maximum, first.val + second.val)
            first = first.next
            second = second.next

        return maximum