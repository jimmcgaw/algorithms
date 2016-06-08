from queue import Queue

import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(66)
        self.assertEqual(len(self.queue), 1)

    def test_dequeue(self):
        items_to_enqueue = [66,77,88,99]
        for i in items_to_enqueue:
            self.queue.enqueue(i)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 66)
        self.assertEqual(len(self.queue), len(items_to_enqueue)-1)

    def test_dequeue_empty_queue(self):
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, "underflow")

if __name__ == '__main__':
    unittest.main()
