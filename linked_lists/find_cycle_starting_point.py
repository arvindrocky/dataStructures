from list_node import ListNode


class Solution:
    '''
    no need to calculate cycle_length, we can do it without cycle_length
    '''
    def detectCycle(self, head: ListNode) -> ListNode:
        p1: ListNode = None
        cycle_length: int = self.get_cycle_length(head)
        if cycle_length:
            p1 = head
            while cycle_length:
                p1 = p1.next
                cycle_length = cycle_length - 1
            while p1 is not head:
                head = head.next
                p1 = p1.next
        return p1

    def get_cycle_length(self, head: ListNode) -> int:
        count: int = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # found a cycle
                fast = fast.next
                count = count + 1
                while fast is not slow:
                    fast = fast.next
                    count = count + 1
                break
        return count


class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        existing = {}
        while head:
            if head not in existing:
                existing[head] = 0
            else:
                return head
            head = head.next
        return None


class Solution2(object):
    def detectCycle(self, head):
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None


class Solution3:
    def detectCycle(self, A):
        if not A:
            return None
        if A.next == None:
            return None

        slow = fast = A
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow != fast:
            return None
        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


class Solution4:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head


l1 = ListNode(10)
l2 = ListNode(20)
l3 = ListNode(30)
l4 = ListNode(40)
l5 = ListNode(50)
l6 = ListNode(60)
l7 = ListNode(70)
l8 = ListNode(80)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l4

sol = Solution()
print("Cycle length is: {}".format(sol.get_cycle_length(l1)))
start_node = sol.detectCycle(l1)
print("Starting node of Cycle is: {}".format(start_node.val) if start_node else "Cycle not found")

sol1 = Solution1()
start_node1 = sol1.detectCycle(l1)
print("Starting node of Cycle is: {}".format(start_node1.val) if start_node1 else "Cycle not found")

sol2 = Solution2()
start_node2 = sol2.detectCycle(l1)
print("Starting node of Cycle is: {}".format(start_node2.val) if start_node2 else "Cycle not found")
