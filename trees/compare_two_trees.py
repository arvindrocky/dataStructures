class Node:
    def __init__(self, value: int = 0, left_child: 'Node' = None, right_child: 'Node' = None):
        self.value = value
        self.left_node = left_child
        self.right_node = right_child


class TreeOperation:
    @staticmethod
    def compare_two_trees(node1: Node, node2: Node) -> bool:
        if not node1 and not node2:
            return True
        if node1 and not node2 or not node1 and node2:
            return False
        if node1.value != node2.value:
            return False
        return TreeOperation.compare_two_trees(node1.left_node, node2.left_node) and TreeOperation.compare_two_trees(
                node1.right_node, node2.right_node)


tree_1 = Node(100, Node(50), Node(60, Node(80), Node(90)))
tree_2 = Node(100, Node(50), Node(60, Node(80), Node(90)))

tree_3 = Node(100, Node(50), Node(60))
tree_4 = Node(100, Node(50), Node(60, Node(80)))

print("Comparing Tree1 and Tree2:")
print(TreeOperation.compare_two_trees(tree_1, tree_2))

print("Comparing Tree3 and Tree4:")
print(TreeOperation.compare_two_trees(tree_3, tree_4))
