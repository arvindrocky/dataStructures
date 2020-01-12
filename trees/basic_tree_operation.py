class Tree:
    def __init__(self, value):
        self.left_node: Tree = None
        self.right_node: Tree = None
        self.value: int = value

    def add_child(self, child, is_left_child: bool = True) -> None:
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


root = Tree(10)
print("Printing tree with only root:")
root.print_tree()

left_child = Tree(20)
root.add_child(left_child)

print("Printing tree with only left child:")
root.print_tree()

right_child = Tree(30)
root.add_child(right_child, False)

print("Printing tree with left and right children:")
root.print_tree()

left_grand_child = Tree(40)
left_child.add_child(left_grand_child)

print("Printing tree with left, right and left grand children:")
root.print_tree()
