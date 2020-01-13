class Node:
    def __init__(self, value: int, left_child: 'Node' = None, right_child: 'Node' = None):
        self.value: int = value
        self.left_node: Node = left_child
        self.right_node: Node = right_child

class BSTOperations:
    def __init__(self):
        pass

    def insert_node(self, bst: Node, value: int) -> Node:
        pass

    def delete_node(self, bst: Node, value: int) -> None:
        pass

    @staticmethod
    def print_in_order_of_tree(node: Node) -> None:
        # left, root, right
        if not node:
            return
        BSTOperations.print_in_order_of_tree(node.left_node)
        print(node.value)
        BSTOperations.print_in_order_of_tree(node.right_node)

    @staticmethod
    def print_in_order_of_tree1(node: Node) -> None:
        # left, root, right
        if node:
            if node.left_node:
                BSTOperations.print_in_order_of_tree1(node.left_node)
            print(node.value)
            if node.right_node:
                BSTOperations.print_in_order_of_tree1(node.right_node)

    @staticmethod
    def print_in_order_of_tree2(node: Node) -> None:
        # left, root, right
        if node:
            BSTOperations.print_in_order_of_tree(node.left_node)
            print(node.value)
            BSTOperations.print_in_order_of_tree(node.right_node)

    @staticmethod
    def print_pre_order_of_tree(node: Node) -> None:
        # root, left, right
        if not node:
            return
        print(node.value)
        BSTOperations.print_pre_order_of_tree(node.left_node)
        BSTOperations.print_pre_order_of_tree(node.right_node)

    @staticmethod
    def print_post_order_of_tree(node: Node) -> None:
        # left, right, root
        if not node:
            return
        BSTOperations.print_post_order_of_tree(node.left_node)
        BSTOperations.print_post_order_of_tree(node.right_node)
        print(node.value)


sample_bst = Node(100, Node(50, Node(40), Node(60)), Node(150, Node(140), Node(160)))

print("Printing In Order of a tree:")
BSTOperations.print_in_order_of_tree(sample_bst)

print("Printing In Order-1 of a tree:")
BSTOperations.print_in_order_of_tree1(sample_bst)

print("Printing In Order-2 of a tree:")
BSTOperations.print_in_order_of_tree2(sample_bst)

print("Printing Pre Order of a tree:")
BSTOperations.print_pre_order_of_tree(sample_bst)

print("Printing Post Order of a tree:")
BSTOperations.print_post_order_of_tree(sample_bst)
