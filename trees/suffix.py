class Node(object):
    def __init__(self):
        self.children = []

    def is_leaf_node(self):
        return len(self.children) == 0

    def add_child(self, value):
        child = SuffixNode(value)
        self.children.append(child)


class SuffixNode(Node):
    def __init__(self, value):
        super(SuffixNode, self).__init__()
        self.set_value(value)

    @classmethod
    def get_endchar(cls):
        return '$'

    def set_value(self, value):
        if type(value) is not str:
            raise TypeError("'value' must be a string of characters")
        self._value = list(value)

    def get_value(self):
        value = self._value
        if self.is_leaf_node():
            value.append(self.__class__.get_endchar())
        return ''.join(value)

class SuffixRootNode(Node):
    """ this is just a special flavor of SuffixNode that does not have any value
    or value logic
    """
    def __init__(self):
        super(SuffixRootNode, self).__init__()


class SuffixTree(object):
    def __init__(self):
        pass
