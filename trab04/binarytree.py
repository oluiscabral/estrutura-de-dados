from node import Node

class BinaryTree:
    def __init__(self):
        self.__nodes = []
        self.__current_glue: Node = None
        self.__i = 0
    
    def size(self):
        return len(self.__nodes)
    
    def empty(self):
        return len(self.__nodes) == 0
    
    def root(self):
        return self.__nodes[0]
    
    def nodes(self):
        return self.__nodes
    
    def depth(node):
        if node.is_root():
            return 0
        else:
            return 1 + self.depth(node.parent())

    def height(node:Node):
        if node.is_external():
            return 0
        else:
            h = 0
            for c in node.children():
                h = max(h, self.height(c))
            return 1 + h
    
    def append(self, num:int):
        if self.empty():
            self.__append_root(num)
        else:
            self.__append_new(num)
    
    def __append_root(self, num:int):
        node = Node(None, num)
        self.__nodes.append(node)
        self.__current_glue = node
    
    def __append_new(self, num:int):
        if self.__current_glue.is_full():
            self.__set_next_glue()
        new_node = Node(self.__current_glue, num)
        self.__append_node(new_node)

    def __set_next_glue(self):
        self.__i += 1
        self.__current_glue = self.__nodes[self.__i]

    def __append_node(self, node):
        self.__nodes.append(node)
        self.__current_glue.append_children(node)

    def preorder(self, node:Node):
        ordered = [node]
        for c in node.children():
            ordered.extend(self.preorder(c))
        return ordered
    
    def order(self, node:Node):
        ordered = []
        if len(node) > 0:
            ordered.extend(self.order(node[0]))
        ordered.append(node)
        if len(node) > 1:
            ordered.extend(self.order(node[1]))
        return ordered
    
    def postorder(self, node: Node):
        ordered = []
        chd = []
        for c in node.children():
            ordered.extend(self.postorder(c))
        ordered.append(node)
        return ordered
    
    def __contains__(self, node:Node) -> bool:
        return node in self.__nodes
    
    def __len__(self):
        return len(self.__nodes)
    
    def __getitem__(self, i):
        return self.__nodes[i]
