
class LinkedList(object):
    def __init__(self):
        pass

class LinkedListItem(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def next(self):
        if self.next_node != None:
            return str(self.next_node.value)
        return self.next_node
