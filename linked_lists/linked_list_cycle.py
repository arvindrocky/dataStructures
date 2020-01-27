from list_node import ListNode
from linked_list_operations import LinkedListOperations


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow: ListNode = head
        fast: ListNode = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


l1 = ListNode(10)
l2 = ListNode(20)
l3 = ListNode(30)
l4 = ListNode(40)
l1.next = l2
l2.next = l3
l3.next = l4
#l3.next = l2

#print(LinkedListOperations.display_linked_list(l1))

sol = Solution()
print(sol.hasCycle(l1))
