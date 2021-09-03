class Node:
    def __init__(self, parent, value: int):
        self.__parent = parent
        self.__value = value
        self.__children = []

    def parent(self):
        return self.__parent

    def value(self):
        return self.__value

    def children(self):
        return self.__children

    def is_root(self):
        return parent is None

    def is_external(self):
        return len(self.__children) == 0
    
    def append_children(self, node: 'Node'):
        if self.is_full():
            raise Exception('Cannot append more than two children to a node.')
        self.__children.append(node)
    
    def is_full(self):
        return len(self.__children) > 1

    def __eq__(self, node):
        if self.parent() != node.parent():
            return False
        if self.value() != node.value():
            return False
        if self.children() != node.children():
            return False
        return True

    def __ne__(self, node):
        return not self.__eq__(node)

    def __lt__(self, node):
        return self.value() < node.value()

    def __gt__(self, node):
        return self.value() > node.value()

    def __le__(self, node):
        return self.value <= node.value()

    def __ge__(self, node):
        return self.value() >= node.value()

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return self.__str__()
        
        
        

    def __len__(self):
        return len(self.__children)

    def __getitem__(self, i):
        return self.__children[i]
