class Stack(object):
    def __init__(self):
        """ we use a list to track internal state. Kind of
        odd since Python lists implement push (aka append) and pop operations
        that manipulate the *end* of the list. This implementation hacks
        it up to manipulate the *start* of the list.

        """
        self.items = []  # list for tracking internal stack state

    def __len__(self):
        return len(self.items)

    def top(self):
        """ return the value of the last item pushed onto the stack
        If the stack is empty, returns False.
        """
        if len(self) == 0:
            return False
        else:
            return self.items[0]

    def push(self, item):
        """ insert an item at the front of our list, at index 0. """
        self.items.insert(0, item)
        return self.items

    def pop(self):
        """ returns the value of the last item pushed onto the stack,
        and removes this value from the stack. If stack is empty, returns
        'underflow'.
        """
        if len(self) == 0:
            return "underflow"
        else:
            return self.items.pop(0)
