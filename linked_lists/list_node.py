# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next_child: 'ListNode' = None):
        self.val = x
        self.next = next_child

    def __repr__(self):
        a = str(self.val)
        if self.next:
            a += " -> " + self.next.__repr__()
        return a
