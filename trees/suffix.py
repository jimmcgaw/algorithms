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

import collections


class SuffixTree(object):
    def __init__(self, value):
        self.rootNode = SuffixRootNode()
        self._iterator = self._create_iteration_generator(value)

    def _create_iteration_generator(self, value):
        """ we create a generator for iterations since a nucleotide string might be massive """
        char_count = len(value)
        start_range = -1
        end_range = char_count - 1
        current_index = start_range
        end_index = -end_range-2
        while True:
            if current_index > end_index:
                yield (value[current_index:], char_count + current_index + 1)
                current_index = current_index - 1
            else:
                yield None

    def get_next_iteration(self):
        return next(self._iterator)

    def construct_tree(self):
        pass
