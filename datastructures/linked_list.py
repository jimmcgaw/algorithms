
class LinkedList(object):
    """
    Manages a (singly) linked list of LinkedListItem objects and their references
    to the next item.

    """
    def __init__(self):
        self.items = []
        self.nextItem = None

    def __len__(self):
        return len(self.items)

    def insert(self, itemValue):
        """ item is inserted into the front of the list """
        if len(self) > 0:
            nextItem = self.items[0]
            item = LinkedListItem(itemValue, next_node=nextItem)
        else:
            item = LinkedListItem(itemValue)
        self.items.insert(0, item)

    def search(self, itemValue):
        matching_items = [item for item in self.items if str(item) == itemValue]
        if len(matching_items) == 0:
            return None
        return matching_items[0]

    def next(self):
        if len(self) > 0:
            if not self.nextItem:
                self.nextItem = self.items[0]
            else:
                self.nextItem = self.nextItem.next_node
            return self.nextItem
        return None

class LinkedListItem(object):
    """
    Holds a string value and an optional reference to the next item.
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

    def setNext(self, next_node):
        self.next_node = next_node

    def next(self):
        if self.next_node != None:
            return str(self.next_node.value)
        return self.next_node
