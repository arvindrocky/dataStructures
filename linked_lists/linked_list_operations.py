from list_node import ListNode


class LinkedListOperations:
    @staticmethod
    def display_linked_list(head: ListNode) -> None:
        list_of_values = list()
        while head:
            list_of_values.append(head.val)
            head = head.next
        print(" -> ".join(map(str, list_of_values)))
