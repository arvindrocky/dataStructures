class Tree:
    def __init__(self, value, left_node: 'Tree' = None, right_node: 'Tree' = None):
        self.left_node: Tree = left_node
        self.right_node: Tree = right_node
        self.value: int = value

    def add_child(self, child: 'Tree', is_left_child: bool = True) -> None:
        if is_left_child:
            self.left_node = child
        else:
            self.right_node = child

    def print_tree(self) -> None:
        print(self.value)
        if self.left_node:
            self.left_node.print_tree()
        if self.right_node:
            self.right_node.print_tree()

    def print_in_order_tree(self) -> None:
        if self.left_node:
            self.left_node.print_in_order_tree()
        print(self.value)
        if self.right_node:
            self.right_node.print_in_order_tree()

    def print_pre_order_tree(self) -> None:
        print(self.value)
        if self.left_node:
            self.left_node.print_pre_order_tree()
        if self.right_node:
            self.right_node.print_pre_order_tree()

    def print_post_order_tree(self) -> None:
        if self.left_node:
            self.left_node.print_post_order_tree()
        if self.right_node:
            self.right_node.print_post_order_tree()
        print(self.value)


tree = Tree(10)
print("Printing tree with only root:")
tree.print_tree()

left_child = Tree(20)
tree.add_child(left_child)

print("Printing tree with only left child:")
tree.print_tree()

right_child = Tree(30)
tree.add_child(right_child, False)

print("Printing tree with left and right children:")
tree.print_tree()

left_grand_child = Tree(40)
left_child.add_child(left_grand_child)

print("Printing tree with left, right and left grand children:")
tree.print_tree()

right_grand_child = Tree(50, Tree(60, Tree(70)))
right_child.add_child(right_grand_child, False)

print("Printing tree with left, right, left grand children and right grand children:")
tree.print_tree()

another_tree = Tree(10, Tree(20, Tree(40), Tree(50)), Tree(30, Tree(60), Tree(70)))
print("Printing In Order of a tree:")
another_tree.print_in_order_tree()

print("Printing In Order of a tree:")
another_tree.print_pre_order_tree()

print("Printing In Order of a tree:")
another_tree.print_post_order_tree()
