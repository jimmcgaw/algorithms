class Queue(object):
    def __init__(self):
        """ index 0 is head of queue, last index is tail of queue """
        self.items = []

    def __len__(self):
        """ usage: q = Queue(); len(q) => 0 """
        return len(self.items)

    def enqueue(self, item):
        """ queues a new item onto the head of the queue """
        self.items.insert(0, item)

    def dequeue(self):
        """ removes oldest item enqueued from the queue """
        if len(self.items) == 0:
            return "underflow"
        return self.items.pop(len(self.items)-1)
