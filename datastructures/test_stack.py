from stack import Stack

import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_top_empty_stack(self):
        latest_item = self.stack.top()
        self.assertEqual(latest_item, False)

    def test_top_with_stack_contents(self):
        items_to_push = [5,9,22]
        for i in items_to_push:
            self.stack.push(i)
        self.assertEqual(self.stack.top(), 22)
        self.assertEqual(len(self.stack), len(items_to_push))

    def test_push(self):
        stack_contents = self.stack.push(1)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(stack_contents, [1])

    def test_pop_with_stack_contents(self):
        items_to_push = [5,9,22]
        for i in items_to_push:
            self.stack.push(i)

        popped_item = self.stack.pop()
        self.assertEqual(popped_item, items_to_push[len(items_to_push)-1])
        self.assertEqual(len(self.stack), len(items_to_push)-1)

    def test_pop_with_empty_stack(self):
        popped_item = self.stack.pop()
        self.assertEqual(popped_item, "underflow")

if __name__ == '__main__':
    unittest.main()
