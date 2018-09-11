from Classes.Node import Node


class Tree:
    def __init__(self, node_item: Node):
        self.NodeData = node_item
        self.LeftTree = None
        self.RightTree = None

    def insert(self, new_node: Node):
        current_node = self.NodeData

        if current_node.Value < new_node.Value:
            if self.LeftTree is None:
                self.LeftTree = Tree(new_node)
            else:
                self.LeftTree.insert(new_node)
        else:
            if self.RightTree is None:
                self.RightTree = Tree(new_node)
            else:
                self.RightTree.insert(new_node)

    def walk_tree(self):
        result = ""

        if self.LeftTree is not None:
            result = self.LeftTree.walk_tree()

        result += "{0}".format(self.NodeData.Value)

        if self.RightTree is not None:
            result += self.RightTree.walk_tree()

        return result


if __name__ == "__main__":
    node = Node(1)
    newTree = Tree(node)
    for i in range(2, 10):
        newTree.insert(Node(i))
    result_new = newTree.walk_tree()

    print(result_new)
