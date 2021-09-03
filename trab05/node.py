class Node:
    def __init__(self, key, parent=None):
        self.parent: 'Node' = parent
        self.key = key
        self.children: List['Node'] = [None, None]
        self.__height: int = 0
        self.__is_modified = False

    def __eq__(self, node):
        if node is None:
            return False
        if self.key != node.key:
            return False
        if self.children != node.children:
            return False
        return True

    def __len__(self):
        return len(self.__iter__())

    def __ne__(self, node):
        return not self.__eq__(node)

    def __lt__(self, node):
        return self.key < node.key

    def __gt__(self, node):
        return self.key > node.key

    def __le__(self, node):
        return self.key <= node.key

    def __ge__(self, node):
        return self.key >= node.key

    def __str__(self):
        return str(self.key)

    def __getitem__(self, i):
        self.__handle_index(i)
        return self.children[i]

    def __iter__(self):
        return iter([child for child in self.children if child is not None])

    def __handle_index(self, i):
        if i > 1:
            raise Exception("Node is binary: has only two children. Index must be -1 < i < 2.")

    def __setitem__(self, i, node):
        self.__handle_index(i)
        self.__set_children(i, node)

    def __set_children(self, i, node):
        self.children[i] = node
        node.parent = self
        self.__is_modified = True

    def height(self):
        if not self.__is_modified:
            return self.__height
        self.__height = 0
        tallest = -1
        for child in self:
            if child.height() > tallest:
                tallest = child.height()
        self.__is_modified = False
        self.__height = tallest + 1
        return self.__height

    def is_balanced(self):
        child_heights = [child.height() for child in self]
        if len(child_heights) == 1:
            return False
        elif len(child_heights) > 0:
            balance = max(child_heights) - min(child_heights)
            return balance > -2 and balance < 2
        return True
