class Node:
    def __init__(self, value: int, left_child: 'Node' = None, right_child: 'Node' = None):
        self.value: int = value
        self.left_node: Node = left_child
        self.right_node: Node = right_child

class BSTOperations:
    def __init__(self):
        pass

    @staticmethod
    def insert_node(node: Node, value: int) -> Node:
        if not node:
            return Node(value)
        if value < node.value:
            node.left_node = BSTOperations.insert_node(node.left_node, value)
        else:
            node.right_node = BSTOperations.insert_node(node.right_node, value)
        return node

    @staticmethod
    def delete_node(node: Node, value: int) -> None:
        if not node:
            print("Unable to find a node to delete")
            return
        if value == node.value:
            return None
        elif value < node.value:
            node.left_node = BSTOperations.delete_node(node.left_node, value)
        else:
            node.right_node = BSTOperations.delete_node(node.right_node, value)
        return node

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

sample_bst1 = Node(100)
BSTOperations.insert_node(sample_bst1, 50)
BSTOperations.insert_node(sample_bst1, 40)
BSTOperations.insert_node(sample_bst1, 60)
BSTOperations.insert_node(sample_bst1, 120)
BSTOperations.insert_node(sample_bst1, 110)
BSTOperations.insert_node(sample_bst1, 130)

print("Printing In Order of a tree after inserting new nodes:")
BSTOperations.print_in_order_of_tree(sample_bst1)

BSTOperations.delete_node(sample_bst1, 60)
print("Printing In Order of a tree after deleting a node:")
BSTOperations.print_in_order_of_tree(sample_bst1)
