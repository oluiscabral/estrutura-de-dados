from typing import List, Set
from node import Node


class BalancedTree:
    def __init__(self):
        self.root = None
        self.__ordered: List[Node] = []
        self.last_node: Node = None

    def insert(self, key) -> None:
        node = Node(key)
        if self.is_empty():
            self.root = node
        else:
            searched = self.search(node)
            if searched.key != node.key:
                if searched.key < node.key:
                    searched[1] = node
                else:
                    searched[0] = node
        self.rebalance(node)

    def is_empty(self):
        return self.root is None

    def search(self, node: Node, root: Node = None):
        self.__handle_node(node)
        root = self.__get_root(root)
        if node.key == root.key:
            return root
        elif node <= root:
            if root[0] is not None:
                return self.search(node, root[0])
        elif root[1] is not None:
            return self.search(node, root[1])
        return root

    def __handle_node(self, node: Node):
        if node is None:
            raise Exception("Cannot search None value as node.")

    def __get_root(self, root: Node):
        if root is None:
            if self.is_empty():
                raise Exception("Cannot search node. Tree is empty.")
            root = self.root
        return root

    def rebalance(self, node: Node):
        is_first = True
        while node is not None:
            last_height = node.height()
            if not node.is_balanced():
                tallest_grandchild = self.__get_tallest_grandchild(node)
                self.restructure(tallest_grandchild)
            if not is_first and node.height() == last_height:
                node = None
            else:
                node = node.parent
                is_first = False

    def __get_tallest_grandchild(self, node):
        if node[0] != None and node[1] != None:
            return max(self.__get_tallest_child(node[0]), self.__get_tallest_child(node[1]))
        elif node[0] != None:
            return self.__get_tallest_child(node[0])
        else:
            return self.__get_tallest_child(node[1])

    def __get_tallest_child(self, node):
        tallest = None
        for child in node:
            if tallest is None or child > tallest:
                tallest = child
        return tallest

    def restructure(self, node: Node):
        if node is None:
            return None
        grandfather = node.parent
        if self.__are_same_side_nodes(node, grandfather):
            self.rotate(grandfather)
            return grandfather
        else:
            self.rotate(node)
            self.rotate(node)  # really 2x
            return node

    def __are_same_side_nodes(self, a: Node, b: Node):
        return self.__is_left_node(a) and self.__is_left_node(b)

    def __is_left_node(self, node):
        return node.parent[0] == node

    def rotate(self, node):
        grandfather = node.parent
        great_granfather = grandfather.parent
        if great_granfather is None:
            self.root = node
        else:
            if grandfather == great_granfather[0]:
                great_granfather[0] = node
            else:
                great_granfather[1] = node
        if node == grandfather[0]:
            grandfather[0] = node[1]
            node[1] = grandfather
        else:
            grandfather[1] = node[0]
            node[0] = grandfather

    def preordered(self):
        self.__ordered.clear()
        self.preorder(self.root)
        return self.__ordered.copy()

    def preorder(self, node):
        if node is None:
            return None
        self.__ordered.append(node)
        for child in node:
            self.preorder(child)

    def ordered(self):
        self.__ordered.clear()
        self.order(self.root)
        return self.__ordered.copy()

    def order(self, node):
        if node is None:
            return None
        self.order(node[0])
        self.__ordered.append(node)
        self.order(node[1])

    def postordered(self):
        self.__ordered.clear()
        self.postorder(self.root)
        return self.__ordered.copy()

    def postorder(self, node):
        if node is None:
            return None
        for child in node:
            self.postorder(child)
        self.__ordered.append(node)
