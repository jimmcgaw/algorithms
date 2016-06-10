from suffix import SuffixNode, SuffixTree, Node, SuffixRootNode

import unittest

class NodeTest(unittest.TestCase):
    def setUp(self):
        self.node = Node()

    def test_is_leaf_node(self):
        """ a leaf node has no children of its own """
        self.node = SuffixNode("C")
        self.assertEqual(self.node.is_leaf_node(), True)
        self.node.add_child("C")
        self.assertEqual(self.node.is_leaf_node(), False)

    def test_add_child(self):
        self.node.add_child("T")
        self.assertEqual( len(self.node.children), 1)


class SuffixNodeTest(unittest.TestCase):
    def setUp(self):
        self.node = SuffixNode("A")
        self.endchar = SuffixNode.get_endchar()

    def test_get_endchar(self):
        self.assertEqual(SuffixNode.get_endchar(), "$")

    def test_initialize_with_value(self):
        self.node = SuffixNode("G")
        self.assertEqual(self.node.get_value(), "G" + self.endchar)

    def test_set_value(self):
        self.node = SuffixNode("A")
        self.node.set_value("T")
        self.assertEqual(self.node.get_value(), "T" + self.endchar)

    def test_set_value_overrides_initial_value(self):
        self.node = SuffixNode("A")
        self.assertEqual(self.node.get_value(), "A" + self.endchar)
        self.node.set_value("C")
        self.assertEqual(self.node.get_value(), "C" + self.endchar)

    def test_set_value_with_invalid_value(self):
        self.assertRaises(TypeError, self.node.set_value, {'py': 'dict'})

    def test_get_value(self):
        """ if not a leaf node, no term character in value """
        self.node = SuffixNode("A")
        self.node.add_child("T")
        self.assertEqual(self.node.get_value(), "A")

    def test_get_value_leaf_node(self):
        self.node = SuffixNode("A")
        self.assertEqual(self.node.is_leaf_node(), True)
        self.assertEqual(self.node.get_value(), "A" + self.endchar)

import collections

class SuffixTreeTest(unittest.TestCase):
    def setUp(self):
        self.nucleotides = u'CAGTCAGG'
        self.tree = SuffixTree(self.nucleotides)

    def test_has_root(self):
        """ we initialize the tree with a root node """
        self.assertTrue(self.tree.rootNode is not None)
        self.assertTrue(isinstance(self.tree.rootNode, SuffixRootNode))

    def test_get_next_iteration(self):
        self.tree = SuffixTree("CAG")
        self.assertTrue(self.tree._iterator is not None)
        self.assertEqual( self.tree.get_next_iteration(), ('G', 3))
        self.assertEqual( self.tree.get_next_iteration(), ('AG', 2))
        self.assertEqual( self.tree.get_next_iteration(), ('CAG', 1))
        # make sure iterator halts when we reach beginning of string
        self.assertEqual( self.tree.get_next_iteration(), None)
        self.assertEqual( self.tree.get_next_iteration(), None)

    def test_construct_tree(self):
        pass
