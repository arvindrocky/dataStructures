from list_node import ListNode
from linked_list_operations import LinkedListOperations


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        temp_node = self.reverseList(head.next)
        if temp_node:
            head.next = None
            tail = temp_node
            while tail.next:
                tail = tail.next
            tail.next = head
        else:
            temp_node = head
        return temp_node


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        head_rev = self.rev_rec(head)  # self.rev_itr(head)
        return head_rev

    def rev_rec(self, head):
        if not head or not head.next:
            # base case- end of list reached
            return head

        prev = self.rev_rec(head.next)
        head.next.next = head
        head.next = None

        return prev


l1 = ListNode(10)
l2 = ListNode(20)
l3 = ListNode(30)
l4 = ListNode(40)

l1.next = l2
l2.next = l3
l3.next = l4

LinkedListOperations.display_linked_list(l1)

sol = Solution()
reversed_list = sol.reverseList(l1)
LinkedListOperations.display_linked_list(reversed_list)
