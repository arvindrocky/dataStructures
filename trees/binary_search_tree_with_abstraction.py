import queue
import sys


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
    def delete_node(node: Node, value: int) -> Node:
        if not node:
            print("Unable to find a node to delete")
            return
        if value == node.value:
            if node.right_node and not node.left_node:
                return node.right_node
            if node.left_node and not node.right_node:
                return node.left_node
            if node.left_node and node.right_node:
                min_node: Node = BSTOperations.find_min_node(node)
                min_node.right_node = node.right_node
                del node
                return min_node
            del node
            return None
        elif value < node.value:
            node.left_node = BSTOperations.delete_node(node.left_node, value)
        else:
            node.right_node = BSTOperations.delete_node(node.right_node, value)
        return node

    @staticmethod
    def find_min_node(node: Node) -> Node:
        if node.left_node:
            return BSTOperations.find_min_node(node.left_node)
        return node

    @staticmethod
    def find_max_node(node: Node) -> Node:
        if node.right_node:
            return BSTOperations.find_max_node(node.right_node)
        return node

    @staticmethod
    def find_in_order_successor_of_a_node(node: Node) -> Node:
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
    def print_in_order_of_tree_using_stack(node: Node) -> None:
        stack = list()
        while True:
            while node:
                stack.append(node)
                node = node.left_node
            if not len(stack):
                break
            node = stack.pop()
            print(node.value)
            node = node.right_node

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

    @staticmethod
    def print_bst_of_tree(node: Node) -> None:
        if not node:
            return
        bst_queue: queue = queue.Queue(0)
        bst_queue.put(node)
        while not bst_queue.empty():
            current_node: Node = bst_queue.get()
            print(current_node.value)
            if current_node.left_node:
                bst_queue.put(current_node.left_node)
            if current_node.right_node:
                bst_queue.put(current_node.right_node)

    @staticmethod
    def print_bst_of_tree_1(node: Node) -> None:
        bst_queue: queue = queue.Queue(0)
        bst_queue.put(node)
        while not bst_queue.empty():
            current_node: Node = bst_queue.get()
            if current_node:
                print(current_node.value)
                bst_queue.put(current_node.left_node)
                bst_queue.put(current_node.right_node)

    @staticmethod
    def print_all_nodes_at_level_k(node: Node, level: int = 1) -> None:
        if not node:
            return
        if level == 1:
            print(node.value)
        else:
            BSTOperations.print_all_nodes_at_level_k(node.left_node, level - 1)
            BSTOperations.print_all_nodes_at_level_k(node.right_node, level - 1)

    @staticmethod
    def print_all_nodes_at_level_k_1(node: Node, level: int = 1, current_level: int = 1) -> None:
        if not node:
            return
        if current_level == level:
            print(node.value)
        else:
            BSTOperations.print_all_nodes_at_level_k_1(node.left_node, level, current_level + 1)
            BSTOperations.print_all_nodes_at_level_k_1(node.right_node, level, current_level + 1)

    @staticmethod
    def print_all_nodes_at_level_k_using_queues(node: Node, level: int = 1) -> None:
        current_level = 1
        bst_queue: queue = queue.Queue(0)
        bst_queue.put(current_level)
        bst_queue.put(node)
        while not bst_queue.empty():
            popped_level: int = bst_queue.get()
            popped_node: Node = bst_queue.get()
            if popped_node:
                if popped_level == level:
                    print(popped_node.value)
                else:
                    bst_queue.put(popped_level + 1)
                    bst_queue.put(popped_node.left_node)
                    bst_queue.put(popped_level + 1)
                    bst_queue.put(popped_node.right_node)

    @staticmethod
    def print_all_nodes_at_level_k_using_queues_1(node: Node, level: int = 1) -> None:
        if not node:
            return
        current_level = 1
        bst_queue: queue = queue.Queue(0)
        bst_queue.put(current_level)
        bst_queue.put(node)
        while not bst_queue.empty():
            popped_level: int = bst_queue.get()
            popped_node: Node = bst_queue.get()
            if popped_level == level:
                print(popped_node.value)
            else:
                if popped_node.left_node:
                    bst_queue.put(popped_level + 1)
                    bst_queue.put(popped_node.left_node)
                if popped_node.right_node:
                    bst_queue.put(popped_level + 1)
                    bst_queue.put(popped_node.right_node)

    @staticmethod
    def is_valid_bst(node: Node, min: int = -1, max: int = sys.maxsize) -> bool:
        if not node:
            return True
        if min < node.value <= max:
            return BSTOperations.is_valid_bst(node.left_node, min, node.value) and BSTOperations.is_valid_bst(
                    node.right_node, node.value, max)
        return False


sample_bst = Node(100, Node(50, Node(40), Node(60)), Node(150, Node(140), Node(160)))

print("Printing In Order of a tree:")
BSTOperations.print_in_order_of_tree(sample_bst)

print("Printing In Order-1 of a tree:")
BSTOperations.print_in_order_of_tree1(sample_bst)

print("Printing In Order-2 of a tree:")
BSTOperations.print_in_order_of_tree2(sample_bst)

print("Printing In Order of a tree using stack:")
BSTOperations.print_in_order_of_tree_using_stack(sample_bst)

print("Printing Pre Order of a tree:")
BSTOperations.print_pre_order_of_tree(sample_bst)

print("Printing Post Order of a tree:")
BSTOperations.print_post_order_of_tree(sample_bst)

sample_bst_1 = Node(100)
BSTOperations.insert_node(sample_bst_1, 50)
BSTOperations.insert_node(sample_bst_1, 40)
BSTOperations.insert_node(sample_bst_1, 60)
BSTOperations.insert_node(sample_bst_1, 120)
BSTOperations.insert_node(sample_bst_1, 110)
BSTOperations.insert_node(sample_bst_1, 130)
BSTOperations.insert_node(sample_bst_1, 150)

print("Printing In Order of a tree after inserting new nodes:")
BSTOperations.print_in_order_of_tree(sample_bst_1)

BSTOperations.delete_node(sample_bst_1, 50)
print("Printing In Order of a tree after deleting a node:")
BSTOperations.print_in_order_of_tree(sample_bst_1)

print("Finding min node")
min_node_of_bst = BSTOperations.find_min_node(sample_bst_1)
print(min_node_of_bst.value)

print("Finding max node")
max_node_of_bst = BSTOperations.find_max_node(sample_bst_1)
print(max_node_of_bst.value)

print("Printing BST of a tree:")
BSTOperations.print_bst_of_tree(sample_bst_1)

print("Printing BST of a tree-1:")
BSTOperations.print_bst_of_tree_1(sample_bst_1)

print("Printing all nodes of a tree at level k:")
BSTOperations.print_all_nodes_at_level_k(sample_bst_1, 3)

print("Printing all nodes of a tree at level k-1:")
BSTOperations.print_all_nodes_at_level_k_1(sample_bst_1, 3)

print("Printing all nodes of a tree at level k using queues:")
BSTOperations.print_all_nodes_at_level_k_using_queues(sample_bst_1, 3)

print("Printing all nodes of a tree at level k using queues-1:")
BSTOperations.print_all_nodes_at_level_k_using_queues_1(sample_bst_1, 3)

print("Validating if a tree is BST or not:")
print(BSTOperations.is_valid_bst(sample_bst))

sample_bst_2 = Node(100, Node(70, Node(110), Node(80)), Node(150, Node(140)))
print("Validating if tree-2 is BST or not:")
print(BSTOperations.is_valid_bst(sample_bst_2))
