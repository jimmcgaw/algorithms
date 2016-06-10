class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def __str__(self):
        return str(self.value)


class BinaryTree(object):
    def __init__(self):
        self.rootNode = None

    def _createNode(self, value):
        """ factory method for creating nodes for our tree """
        return BinaryTreeNode(value)

    def _insertChildNode(self, childNode, parentNode):
        """
        recursively called method that inserts a child node to a given parent node.
        If the value of new child node is less than the parent, we check the left child
        node. If left child is None, we insert the new node there.
        If left child exists, recursively call this method with that child node.
        The same logic applies for the right child, in the case where the new
        """
        if childNode.value < parentNode.value:
            if parentNode.left_child is not None:
                self._insertChildNode(childNode, parentNode.left_child)
            else:
                parentNode.left_child = childNode
        else:
            if parentNode.right_child is not None:
                self._insertChildNode(childNode, parentNode.right_child)
            else:
                parentNode.right_child = childNode

    def _searchForChildNode(self, value, parentNode):
        if value == parentNode.value:
            return parentNode  # if match, we have the node we want
        # otherwise, compare values
        elif value < parentNode.value and parentNode.left_child is not None:
            return self._searchForChildNode(value, parentNode.left_child)
        elif value > parentNode.value and parentNode.right_child is not None:
            return self._searchForChildNode(value, parentNode.right_child)

    def search(self, value):
        if self.rootNode is not None:
            if self.rootNode.value == value:
                return self.rootNode
            else:
                return self._searchForChildNode(value, self.rootNode)
        else:
            return None

    def insert(self, value):
        newNode = self._createNode(value)
        if not self.rootNode:
            self.rootNode = newNode
        else:
            """ already have a root node, append as child """
            self._insertChildNode(newNode, self.rootNode)

    def _walkNode(self, node):
        if node is not None:
            if node.left_child is not None and node.right_child is not None:
                return [self._walkNode(node.left_child), [node.value], self._walkNode(node.right_child)]
            elif node.left_child is not None:
                return [self._walkNode(node.left_child), [node.value]]
            elif node.right_child is not None:
                return [[node.value], self._walkNone(node.right_child)]
            else:
                return [node.value]
        else:
            return []



    def inorder_tree_walk(self):
        values = []
        value = self._walkNode(self.rootNode)
        if type(value) is list:
            values += value
        elif type(value) is int:
            values.append(value)
        return [val for sublist in values for val in sublist]
