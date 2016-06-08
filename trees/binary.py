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
            if parentNode.left_child != None:
                self._insertChildNode(childNode, parentNode.left_child)
            else:
                parentNode.left_child = childNode
        else:
            if parentNode.right_child != None:
                self._insertChildNode(childNode, parentNode.right_child)
            else:
                parentNode.right_child = childNode

    def insert(self, value):
        newNode = self._createNode(value)
        if not self.rootNode:
            self.rootNode = newNode
        else:
            """ already have a root node, append as child """
            self._insertChildNode(newNode, self.rootNode)
