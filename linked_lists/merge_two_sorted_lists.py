from list_node import ListNode
from linked_list_operations import LinkedListOperations


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        head = self.merge_two_lists_helper(l1, l2, None, None)
        return head

    def merge_two_lists_helper(self, l1: ListNode, l2: ListNode, head: ListNode, tail: ListNode):
        if l1 is None and l2 is None:
            return head
        if 11 is None:
            l2, head, tail = self.append_node(l2, head, tail)
            return head
        if l2 is None:
            l1, head, tail = self.append_node(l1, head, tail)
            return head
        if l1.val < l2.val:
            l1, head, tail = self.append_node(l1, head, tail)
        elif l2.val < l1.val:
            l2, head, tail = self.append_node(l2, head, tail)
        else:
            l1, head, tail = self.append_node(l1, head, tail)
            l2, head, tail = self.append_node(l2, head, tail)
        return self.merge_two_lists_helper(l1, l2, head, tail)

    def append_node(self, node: ListNode, head: ListNode, tail: ListNode):
        if not head:
            # head, tail = ListNode(node.val)
            head = node
            tail = node
        else:
            # tail.next = ListNode(node.val)
            tail.next = node
            tail = tail.next
        return node.next, head, tail


l1 = ListNode(10)
l2 = ListNode(20)
l3 = ListNode(30)
l4 = ListNode(40)

l1.next = l2
l2.next = l3
l3.next = l4

n1 = ListNode(11)
n2 = ListNode(20)
n3 = ListNode(25)
n4 = ListNode(40)
n5 = ListNode(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

LinkedListOperations.display_linked_list(l1)
LinkedListOperations.display_linked_list(n1)

sol = Solution()
merged_list = sol.mergeTwoLists(l1, n1)
LinkedListOperations.display_linked_list(merged_list)
