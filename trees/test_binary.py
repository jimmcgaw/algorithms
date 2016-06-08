from binary import BinaryTree, BinaryTreeNode

import unittest

class BinaryTreeNodeTest(unittest.TestCase):
    def setUp(self):
        self.node = BinaryTreeNode(6)

    def test_node_value(self):
        self.assertEqual(str(self.node), str(6))

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def test_root_node(self):
        """ a tree with a single node will have a root node with no children """
        self.tree.insert(6)
        self.assertEqual(str(self.tree.rootNode), str(6))

    def test_root_node_with_children(self):
        self.tree.insert(6)
        self.tree.insert(3) # should become rootNode's left child
        self.tree.insert(8) # should become rootNode's right child
        self.assertEqual(str(self.tree.rootNode.left_child), str(3))
        self.assertEqual(str(self.tree.rootNode.right_child), str(8))

    def test_tree_with_three_levels(self):
        self.tree.insert(6)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(5)
        self.tree.insert(2)
        self.tree.insert(7)
        self.tree.insert(11)
        self.assertEqual(str(self.tree.rootNode.left_child.right_child), str(5))
        self.assertEqual(str(self.tree.rootNode.left_child.left_child), str(2))
        self.assertEqual(str(self.tree.rootNode.right_child.left_child), str(7))
        self.assertEqual(str(self.tree.rootNode.right_child.right_child), str(11))

    def test_tree_with_three_levels(self):
        """ in the case of an insertion tie comparison test, child node becomes
        the right_child node of the parent with the same value.
        """
        self.tree.insert(6)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(8)
        self.assertEqual(str(self.tree.rootNode.right_child.right_child), str(8))

if __name__ == '__main__':
    unittest.main()
