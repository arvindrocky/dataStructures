class BST:
    def __init__(self, value):
        self.value = value
        self.left_node: BST = None
        self.right_node: BST = None

    def insert_node(self, value: int) -> None:
        if value < self.value:
            if self.left_node:
                self.left_node.insert_node(value)
            else:
                self.left_node = BST(value)
        else:
            if self.right_node:
                self.right_node.insert_node(value)
            else:
                self.right_node = BST(value)
        pass

    def print_in_order_tree(self) -> None:
        if self.left_node:
            self.left_node.print_in_order_tree()
        print(self.value)
        if self.right_node:
            self.right_node.print_in_order_tree()


bst = BST(100)

print("Printing tree with only root:")
bst.print_in_order_tree()

bst.insert_node(50)
bst.insert_node(150)
bst.insert_node(20)
bst.insert_node(125)
bst.insert_node(130)

print("Printing In Order of a tree:")
bst.print_in_order_tree()
