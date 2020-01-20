class Node:
    def __init__(self, value: int = 0, left_child: 'Node' = None, right_child: 'Node' = None):
        self.value = value
        self.left_node = left_child
        self.right_node = right_child


class TreeOperations:
    def __init__(self):
        pass

    @staticmethod
    def print_in_order_of_tree(root_node: Node):
        if not root_node:
            return
        TreeOperations.print_in_order_of_tree(root_node.left_node)
        print(root_node.value)
        TreeOperations.print_in_order_of_tree(root_node.right_node)


class TreeIterator:
    def __init__(self, root_node: Node):
        self.stack = list()
        self.push_next_n_in_order_nodes(root_node)

    def push_next_n_in_order_nodes(self, node: Node) -> None:
        while node:
            self.stack.append(node)
            node = node.left_node

    def is_stack_empty(self) -> bool:
        return len(self.stack) == 0

    def get_next_node(self) -> Node:
        if self.is_stack_empty():
            return None
        current_node: Node = self.stack.pop()
        self.push_next_n_in_order_nodes(current_node.right_node)
        return current_node


class TreeComparator:
    def __init__(self):
        pass

    @staticmethod
    def compare_in_order_of_two_trees(root_1: Node, root_2: Node) -> bool:
        tree_iterator_1 = TreeIterator(root_1)
        tree_iterator_2 = TreeIterator(root_2)
        while not tree_iterator_1.is_stack_empty():
            if tree_iterator_2.is_stack_empty():
                return False
            tree_1_node = tree_iterator_1.get_next_node()
            tree_2_node = tree_iterator_2.get_next_node()
            if tree_1_node.value == tree_2_node.value:
                continue
            return False
        return tree_iterator_2.is_stack_empty()


tree_1 = Node(100, Node(50), Node(60))
tree_2 = Node(60, Node(100, Node(50)))

print("Printing In Order of Tree1:")
TreeOperations.print_in_order_of_tree(tree_1)
print("Printing In Order of Tree2:")
TreeOperations.print_in_order_of_tree(tree_2)
print("Comparing In Order of 2 Trees:")
print(TreeComparator.compare_in_order_of_two_trees(tree_1, tree_2))

tree_3 = Node(100, Node(50), Node(60, Node(80), Node(90)))
tree_4 = Node(100, Node(50), Node(60, Node(80), Node(90)))
print("Printing In Order of Tree3:")
TreeOperations.print_in_order_of_tree(tree_3)
print("Printing In Order of Tree4:")
TreeOperations.print_in_order_of_tree(tree_4)
print("Comparing In Order of 2 Trees:")
print(TreeComparator.compare_in_order_of_two_trees(tree_3, tree_4))

tree_5 = Node(100, Node(50), Node(60))
tree_6 = Node(100, Node(50), Node(60, Node(80)))
print("Printing In Order of Tree5:")
TreeOperations.print_in_order_of_tree(tree_5)
print("Printing In Order of Tree6:")
TreeOperations.print_in_order_of_tree(tree_6)
print("Comparing In Order of 2 Trees:")
print(TreeComparator.compare_in_order_of_two_trees(tree_5, tree_6))
